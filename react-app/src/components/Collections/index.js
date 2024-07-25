import React, { useEffect,  useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getUserCollectionsThunk, getCollectionMessagesThunk, sendQueryThunk, uploadFileThunk } from "../../store/users";
import "./collections.css"
import CreateCollectionModal from "../CreateCollectionModal";
import { OpenModalButton } from "../OpenModalButton";
import CollectionDetailsModal from "../CollectionDetailsModal";
function Collection() {
  const sessionUser = useSelector((state) => state.session.user);
  const collections = useSelector((state => state.users.collections));
  // const currCollection = useSelector((state) => state.users.currCollection);
  const [currentCollectionId, setCurrCollectionId] = useState(false);
  const messages = useSelector((state) => state.users.messages)
  const dispatch = useDispatch()
  const [showMessages, setShowMessages] = useState(1);
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
    console.log('in query submit');
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
  if(Object.keys(collections).length === 0 || Object.keys(messages).length === 0)  {
    return (
      <div>Loading</div>
    )
  }
  else {
    return (
        <div className="collections-container" >

            <div className="collections-list">
              {collections.map((collection) => (
                <div>
                  <button key={collection.id} onClick={() => loadCollection(collection.id)}>
                      {collection.title}

                  </button>
              </div>
              ))}

              <OpenModalButton
                buttonText="Create Collection"
                modalComponent={<CreateCollectionModal />}
              />
            </div>

            <div className="main-container">
              {currentCollectionId &&
              <div className="collection-header">{collections[currentCollectionId-1].title}
                <OpenModalButton
                buttonText="..."
                modalComponent={<CollectionDetailsModal currentCollectionId={currentCollectionId} />}
                />
                <div>
                    <form onSubmit={fileSubmit}>
                    <input
                      type="file"
                      accept="/*"
                      onChange={handleChange}/>
                    <button type="submit">Upload</button>
                  </form>
                </div>

              </div>}
              <div className="query-container">
                {showMessages && currentCollectionId &&(messages != null) &&
                  <div>
                    {/* {collections[toString(currentCollectionId)].title} */}
                    {/* {collections[currentCollectionId].title} */}
                    { messages.map((message) => (
                      <div key={message.id}>
                        {message.content}
                      </div>
                    ))}
              </div>}
            </div>
            <div className="input-container">
                <div className="text-container">
                  <form onSubmit={querySubmit}>
                    <textarea className="textbox"
                    value={content}
                    preview="preview"
                    placeholder="Enter your query here"
                    onChange={(e) => setContent(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === "Enter") {
                        e.preventDefault()
                        querySubmit(e);
                      }
                    }}
                    />

                  </form>
                </div>
                {/* <div>Upload File:
                    <form onSubmit={fileSubmit}>
                    <input
                      type="file"
                      accept="/*"
                      onChange={handleChange}/>
                    <button type="submit">Upload</button>
                  </form>
                </div> */}
              </div>
            </div>
        </div>

      );
  }
}

export default Collection;
