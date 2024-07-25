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

    const collectionTitles = collections.map(collection => collection.name)
    console.log('id', currentCollectionId);

    const handleSubmit = async(e) => {
        e.preventDefault();
        const collection = {

        }

        dispatch(createCollectionThunk(collection));

        closeModal();
    }
    const cancelCreate = () => {
        setErrors([])
        closeModal();
    }

    console.log('collections', currentCollectionId);
    return (
        <div className='collection-modal'>
            <div>File list:</div>
            {/* <div>{currentCollectionId} </div> */}
            <ul>
            {currentCollectionId && collections[currentCollectionId-1].datafiles.map((datafile) => (
                  <li>{datafile.title}</li>
                ))}
            </ul>
        </div>
    )
};

export default CollectionDetailsModal;
