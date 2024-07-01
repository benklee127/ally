import React, { useEffect,  useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getUserCollectionsThunk, getCollectionMessagesThunk, sendQueryThunk, uploadFileThunk } from "../../store/users";


function Collection() {
  const sessionUser = useSelector((state) => state.session.user);
  const collections = useSelector((state => state.users.collections));
  const [currentCollectionId, setCurrCollectionId] = useState(1);
  const messages = useSelector((state) => state.users.messages)
  const dispatch = useDispatch()
  const [showMessages, setShowMessages] = useState(false);
  const [content, setContent] = useState('');
  const [file, setFile] = useState(undefined);



  useEffect(() => {
    dispatch(getUserCollectionsThunk());
    dispatch(getCollectionMessagesThunk(1))
  }, [dispatch], showMessages);

  const loadCollection = (collection_id) => {
    dispatch(getCollectionMessagesThunk(collection_id));
    setCurrCollectionId(collection_id);
    setShowMessages(true)
  }

  const querySubmit = async(e) => {
    e.preventDefault();
    let newQuery = {
      content: content,
      user_id: sessionUser.id,
      collection_id: currentCollectionId,
    }
    dispatch(sendQueryThunk(newQuery,newQuery.collection_id))
    setContent('')
  }
  const handleChange = (event) => {
    setFile(event.target.files[0]);
  };

  const fileSubmit = async(e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('collection_id', currentCollectionId)

    dispatch(uploadFileThunk(formData, currentCollectionId))
  }

  console.log('collections: ', collections);
  if(Object.keys(collections).length === 0  ) {
    return (
      <div>No collections yet</div>
    )
  }else {
    return (
        <div className="collection-list">
            Collection List:
            {collections.map((collection) => (
              <div>
                <button key={collection.id} onClick={() => loadCollection(collection.id)}>
                    {collection.title}

                </button>
            </div>
            ))}
            {showMessages && (messages != null) &&
              <div>
                {/* {collections[currentCollectionId].title} */}
                { messages.map((message) => (
                  <div key={message.id}>
                    {message.content}
                  </div>
                ))}
                <div>Enter Query:
                  <form onSubmit={querySubmit}>
                    <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    />
                    <button type="submit">Submit</button>
                  </form>
                </div>
              </div>}
              <div>Upload File:
                <form onSubmit={fileSubmit}>
                <input
                  type="file"
                  accept="/*"
                  onChange={handleChange}/>
                <button type="submit">Upload</button>
              </form>
              </div>
        </div>
    );
}
}

export default Collection;
