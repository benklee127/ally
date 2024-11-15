import React, { useEffect,  useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getUserCollectionsThunk, getCollectionMessagesThunk, sendQueryThunk, uploadFileThunk} from "../../store/users";
import { loadCollectionThunk } from "../../store/collection";
import "./collections.css"
import CreateCollectionModal from "../CreateCollectionModal";
import { OpenModalButton } from "../OpenModalButton";
import CollectionDetailsModal from "../CollectionDetailsModal";
import ReactMarkdown from 'react-markdown';
import Markdown from 'react-markdown'

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
    dispatch(loadCollectionThunk(collection_id))
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
                <div className="collection-button">
                  <button key={collection.id} onClick={() => loadCollection(collection.id)}>
                      {collection.title}

                  </button>
              </div>
              ))}
              <div id="create-collection-button" className="collection-button">
              <OpenModalButton
                buttonText="+"
                modalComponent={<CreateCollectionModal />}
              /> </div>
            </div>

            <div className="main-container">
              {currentCollectionId &&
              <div className="collection-header">{collections[currentCollectionId-1].title}
                <OpenModalButton
                buttonText="..."
                modalComponent={<CollectionDetailsModal currentCollectionId={currentCollectionId} />}
                />
                <div >
                  <form onSubmit={fileSubmit} className="upload-form">
                    <input
                      type="file"
                      accept="/*"
                      onChange={handleChange}/>
                    <button type="submit" class='upload-button'>Upload</button>
                  </form>
                </div>

              </div>}
              <div className="query-container">
                {showMessages && currentCollectionId &&(messages != null) &&
                  <div>
                    {/* {collections[toString(currentCollectionId)].title} */}
                    {/* {collections[currentCollectionId].title} */}
                    { messages.map((message) => (
                      <div className="message" key={message.id}>
                        <div className="image-column">
                          <div className="image-wrapper">
                            <img src={message.user.profile_photo} />
                          </div>
                        </div>
                        <div className="message-column">
                        <div className="message-header">
                          <div className="message-name-date-wrapper">
                              {message.user.id != sessionUser.id ? "AllyBot" : "You"}
                              <div className="message-date">{message.created_at}</div>
                          </div>

                          </div>
                          <div className="message-content"><Markdown>{message.content}</Markdown></div>
                        </div>
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
