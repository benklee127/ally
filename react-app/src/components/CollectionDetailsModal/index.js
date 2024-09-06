import React, {useState} from "react";
import { useModal } from "../../context/Modal";
import { useDispatch, useSelector } from "react-redux";
import { createCollectionThunk } from "../../store/users";
import './collectionDetails.css'


function CollectionDetailsModal({currentCollectionId}) {
    const dispatch = useDispatch();
    const collections = useSelector((state) => state.users.collections)

    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();
    const user = useSelector(state => state.session.user)
    const [selectedMenu, setSelectedMenu] = useState(1);

    const collectionTitles = collections.map(collection => collection.name)
    console.log('id', currentCollectionId);

    const [editTitle, setEditTitle] = useState(false);
    const [editDesc, setEditDesc] = useState(false);
    const [editModel, setEditModel] = useState(false);


    const handleSubmit = async(e) => {
        e.preventDefault();
        const collection = {
          // title: title,
          // description: description,
          // model: model,
        }

        dispatch(createCollectionThunk(collection));

        closeModal();
    }
    const cancelCreate = () => {
        setErrors([])
        closeModal();
    }

    console.log('collections in details', collections[1].title);
    return (
        <div className='create-channel-modal'>
          <div className="channel-card-header-wrapper">
            <div className= "cc-header">
                {collections[1].title}
            </div>
            
            <div className="cc-header-menu">
              <div className="cc-header-menu-option-wrapper">
                <div
                  className={
                    "cc-header-menu-option" +
                    (selectedMenu === 1 ? "-selected" : "")
                  }
                  onClick={() => setSelectedMenu(1)}
                >
                  About
                </div>
              </div>
              <div className="cc-header-menu-option-wrapper">
                <div
                  className={
                    "cc-header-menu-option" +
                    (selectedMenu === 2 ? "-selected" : "")
                  }
                  onClick={() => setSelectedMenu(2)}
                >
                  Files
                </div>
              </div>
        
              <div className="cc-header-menu-option-wrapper">
                <div
                  className={
                    "cc-header-menu-option" +
                    (selectedMenu === 3 ? "-selected" : "")
                  }
                  onClick={() => setSelectedMenu(3)}
                >
                  Settings
                </div>
              </div>
           
            </div>
        
            {console.log("menu", selectedMenu)}
          </div>
          <div className="collection-body">
              {selectedMenu == 1 ? (
                  <div > Collection details
              
                  </div>
                  
              ): selectedMenu == 2 ? (
                  <div className="channel-form"> 
                          {currentCollectionId && collections[currentCollectionId-1].datafiles.map((datafile) => (
                          <div className="cc-form-item">{datafile.title}</div>
                      ))}
                  </div>
              ) : (
                  <div className="channel-form">
                      <div className="cc-form-item"></div>
                </div>
              )
              }
            </div>
        </div>
    )
};

export default CollectionDetailsModal;
