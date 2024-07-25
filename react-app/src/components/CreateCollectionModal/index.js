import React, {useState} from "react";
import { useModal } from "../../context/Modal";
import { useDispatch, useSelector } from "react-redux";
import { createCollectionThunk } from "../../store/users";
import './createCollection.css'


function CreateCollectionModal() {
    const dispatch = useDispatch();
    const collections = useSelector((state) => state.users.collections)
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [embedding, setEmbedding] = useState("");
    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();
    const user = useSelector(state => state.session.user)

    const collectionTitles = collections.map(collection => collection.name)

    const handleSubmit = async(e) => {
        e.preventDefault();
        const collection = {
            title: title,
            description: description,
            user_id: user.id,
            embedding: embedding
        }

        dispatch(createCollectionThunk(collection));

        closeModal();
    }
    const cancelCreate = () => {
        setErrors([])
        closeModal();
    }

    return (
        <div className='collection-modal'>
            <div className='collection-form'>
                <div className='form-header'>Title:
                <textarea
                    className='form-input'
                    value={title}
                    minLength={1}
                    maxLength={50}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                    />

                </div>

                <div className='form-header'>
                    Description:
                    <textarea
                        className='form-input'
                        value={description}
                        maxLength={50}
                        onChange={(e) => setDescription(e.target.value)}/>
                </div>

                <div className='form-header'>
                    Embedding:
                    <select className='form-input'>
                        <option value="1">embedding</option>
                        <option value="2">elasticsearch</option>
                    </select>
                </div>

                <div>
                    <div onClick={handleSubmit}>Create</div>
                    <div onClick={cancelCreate}>Cancel</div>
                </div>
            </div>

        </div>
    )
};

export default CreateCollectionModal;
