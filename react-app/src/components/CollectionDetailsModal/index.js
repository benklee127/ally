import React, {useEffect, useState, useRef } from "react";
import { useModal } from "../../context/Modal";
import { useDispatch, useSelector } from "react-redux";
import { createCollectionThunk, updateCollectionThunk, uploadFileThunk } from "../../store/users";
import './collectionDetails.css'


function CollectionDetailsModal({currentCollectionId, menuoption}) {
    const dispatch = useDispatch();
    const collections = useSelector((state) => state.users.collections)

    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();
    const user = useSelector(state => state.session.user)
    const [selectedMenu, setSelectedMenu] = useState(menuoption);

    const collectionTitles = collections.map(collection => collection.name)
    console.log('id', currentCollectionId);

    const currCollection = useSelector((state => state.collections.currCollection))
    const [editTitle, setEditTitle] = useState(false);
    const [editDesc, setEditDesc] = useState(false);
    const [editResLlm, setEditResLlm] = useState(false);

    const [showLlmMenu, setShowLlmMenu] = useState(false);
    const [resLlm, setResLlm] = useState(currCollection.res_llm);
    const ulRef = useRef();
    const [title, setTitle] = useState(currCollection.title);
    const [description, setDescription] = useState(currCollection.description);
    const [file, setFile] = useState(undefined);

    const [url, setUrl] = useState(undefined);

    const handleChange = (event) => {
      setFile(event.target.files[0]);
    };
  

    const toggleEditTitle = () => {
      setErrors([]);
      setEditTitle(true);
    };
  
    const toggleEditDesc = () => {
      setErrors([]);
      setEditDesc(true);
    };

    const toggleEditResLlm = () => {
      setErrors([]);
      setEditResLlm(true);
    }

    const fileSubmit = async(e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('collection_id', currentCollectionId)
    
        dispatch(uploadFileThunk(formData, currentCollectionId))
      }

    const closeLlmMenu = () => setShowLlmMenu(false);

    const updateResLLm = (res_llm) => {
      setResLlm(res_llm)
      console.log("resllm updated to", res_llm)
      setShowLlmMenu(false)
      
    }

    const handleSubmit = async(e) => {
        e.preventDefault();
        const newCollection = {
          title: title,
          description: description,
          res_llm: resLlm
        }
        let data;

        data = await dispatch(updateCollectionThunk(newCollection, currCollection.id));

        closeModal();
    }
    const cancelCreate = () => {
        setErrors([])
        closeModal();
    }

    const discardChanges = () => {
      setErrors([]);
      setEditTitle(false);
      setEditDesc(false);
      setEditResLlm(false);
    };
  

    console.log('collections in details', collections[1].title);
    return (
        <div className='create-channel-modal'>
          <div className="channel-card-header-wrapper">
            <div className= "cc-header">
                {currCollection.title}
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
                  Add Documents
                </div>
              </div>
           
            </div>
        
            {console.log("menu", selectedMenu)}
        </div>
        <div className="collection-body">
              {selectedMenu == 1 ? (
                <div onSubmit={handleSubmit} className="channel-form">
                  <div className="cc-form-item" onClick={() => toggleEditTitle()}> 
                    <div className="form-input-header">
                      <div className="form-header-title"> Title </div>
                      {editTitle ? (
                        <div 
                          className={
                            "char-counter" +
                            (title.length >= 20 || title.length <= 2 ? "-max" : "")
                          }
                        >
                          {" "}
                          {title.length + "/20"}
                        </div>
                      ) : (
                        ""
                      )}
                    </div>
                    {editTitle ? (
                      <textarea
                        type="textarea"
                        value={title}
                        minLength={1}
                        maxLength={20}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                      />
                    ) : (
                      <div >{currCollection.title}</div>
                    )}
                  </div>
                  <div className="cc-form-item" onClick={() => toggleEditDesc()}>
                    <div className="form-input-header">
                      <div className="form-header-title">Description</div>

                      {editDesc ? (
                        <div
                          className={"char-counter" + (description.length >= 100 ? "-max" : "")}
                          >
                          {" "}
                          {description.length + "/100"}
                        </div>
                        ) : (
                          ""
                      )}
                    </div>
                    {editDesc ? (
                      <textarea
                        type="textarea"
                        value={description}
                        maxLength={100}
                        onChange={(e) => setDescription(e.target.value)}
                        />
                        ) : (
                          currCollection.description
                      )}
                  </div>
                  <div  className="cc-form-item"   onClick={() => toggleEditResLlm()} >
                    <div className="form-input-header">
                      <div className="form-header-title">Model</div>
              
                    
                      </div>
                      {
                        currCollection.res_llm == "gpt3_5" ?  "ChatGPT 3.5" : 
                        currCollection.res_llm == "gpt4o" ? "ChatGPT 4o" : 
                        currCollection.res_llm == "gpt4o_mini" ? "ChatGPT 4o mini" : 
                        currCollection.res_llm == "gpt4_turbo" ? "ChatGPT 4 Turbo" :
                        "error" 
                      }
                      
                      <div className={showLlmMenu ? "llm-dropdown" : ""}>
                          {editResLlm ? 
                          <div>
                            <div className="llm-dropdown-item"></div>
                            {resLlm != "gpt3_5" ? <div className="llm-dropdown-item" onClick={()=>updateResLLm("gpt3_5")}>ChatGPT 3.5</div> : <div className="llm-dropdown-item selected-llm">ChatGPT 3.5</div> }
                            {resLlm != "gpt4o" ? <div className="llm-dropdown-item" onClick={()=>updateResLLm("gpt4o")}>ChatGPT 4o</div> : <div className="llm-dropdown-item selected-llm">ChatGPT 4o</div> }
                            {resLlm != "gpt4o_mini" ? <div className="llm-dropdown-item" onClick={()=>updateResLLm("gpt4o_mini")}>ChatGPT 4o mini</div> : <div className="llm-dropdown-item selected-llm">ChatGPT 4o mini</div> }
                            {resLlm != "gpt4_turbo" ? <div className="llm-dropdown-item" onClick={()=>updateResLLm("gpt4_turbo")}>ChatGPT 4 Turbo</div> : <div className="llm-dropdown-item selected-llm">ChatGPT 4 Turbo</div> }
                            </div>
                          : <></>}
                        </div>
                  </div>

                {  (editDesc || editTitle || editResLlm)? (
                  <div className="cc-form-item-save">
                      <div className="cc-update-buttons">
                        <div className="cc-update-save" onClick={handleSubmit}>
                          Save
                        </div>
                        <div className="cc-update-cancel" onClick={discardChanges}>
                          Cancel
                        </div>
                      </div>
                  </div>
                ) : (
                  ""
                )} 

          </div>
          
        ): selectedMenu == 2 ? (
                  <div className="channel-form"> 
                          {currentCollectionId && collections[currentCollectionId-1].datafiles.map((datafile) => (
                          <div className="cc-form-item">
                            {datafile.title}
                            <div>Delete</div>
                            <div>Manage (WIP)</div>
                          </div>
                      ))}
                  </div>
              ) : (
                <div className="channel-form">
                  <div className="cc-form-item">
                    <form onSubmit={fileSubmit} className="upload-form">
                      <input
                        type="file"
                        accept="/*"
                        onChange={handleChange}/>
                      {file ? <button type="submit" className='upload-button' >Upload</button> : ""}
                    </form>
                  </div>
                  <div className="cc-form-item">
                    Web Url
                  </div>
                </div>
                //   <div className="channel-form">
                //       <div className="cc-form-item" id="llm_dropdown" onClick={()=>toggleEditResLlm()}>
                //         {(currCollection.res_llm == "gpt3_5") ?
                //             "ChatGPT 3.5" :
                //             (currCollection.res_llm == "gpt4o") ?
                //             "ChatGPT 4o":
                //             (currCollection.res_llm == "gpt4o_mini") ?
                //             "ChatGPT 4o mini":
                //             (currCollection.res_llm == "gpt4_turbo") ?
                //             "ChatGPT 4 Turbo":
                //             "error"
                //         }
                //       </div>
                //       {editResLlm ? 
                //       <div>
                        
                //         {resLlm != "gpt3_5" ? <div className="cc-form-item" onClick={()=>updateResLLm("gpt3_5")}>ChatGPT 3.5</div> : <></> }
                //         {resLlm != "gpt4o" ? <div className="cc-form-item" onClick={()=>updateResLLm("gpt4o")}>ChatGPT 4o</div> : <></> }
                //         {resLlm != "gpt4o_mini" ? <div className="cc-form-item">ChatGPT 4o mini</div> : <></> }
                //         {resLlm != "gpt4_turbo" ? <div className="cc-form-item">ChatGPT 4 Turbo</div> : <></> }
                //         </div>
                //       : <></>}
                //        {showLlmMenu ? 
                //         <div className="cc-update-buttons">
                //           <div className="cc-update-save" onClick={handleSubmit}>
                //             Save
                //           </div>
                //           {/* <div className="cc-update-cancel" onClick={discardChanges}>
                //             Cancel
                //           </div> */}
                //         </div>
                //       : <></>}
                // </div>
              )
              }
            
            </div>
            
            
        </div>
    )
};

export default CollectionDetailsModal;
