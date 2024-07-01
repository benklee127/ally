const GET_ALL_COMMENTS = "comment/GET_ALL_COMMENTS";
const CREATE_COMMENT = "comment/CREATE_COMMENT";
const UPDATE_COMMENT = "comment/UPDATE_COMMENT";
const DELETE_COMMENT = "comment/DELETE_COMMENT";
const GET_SINGLE_COMMENT = "comment/GET_SINGLE_COMMENT";

const getAllComments = (comments) => ({
    type: GET_ALL_COMMENTS,
    comments,
});

const createComment = (comment) => ({
    type: CREATE_COMMENT,
    comment,
});

const updateComment = (comment) => ({
    type: UPDATE_COMMENT,
    comment,
});

const deleteComment = (comment) => ({
    type: DELETE_COMMENT,
    comment,
});

const getSingleComment = (comment) => ({
    type: GET_SINGLE_COMMENT,
    comment,
})


export const deleteCommentThunk = (comment) => async (dispatch) => {

        const res = await fetch(`/api/comments/${comment.id}/delete`, {
            method: "DELETE",
        });
        if (res.ok) {
            dispatch(deleteComment(comment));
            return;
        }
};



export const updateCommentThunk = (comment, id) => async (dispatch) => {
    // try {
        const res = await fetch(`/api/comments/update/${id}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(comment),
        });

        // console.log('responde in update', res)
        if (res.ok) {
            const updatedComment = await res.json();
            dispatch(updateComment(updatedComment));
            return updatedComment;
        }
    // } catch (err) {
    //     const errors = err.json();
    //     return errors;
    // }
};


export const createCommentThunk = (image_id, user_id, comment) => async (dispatch) => {
    try {
        const res = await fetch(`/api/comments/${image_id}/${user_id}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(comment),
        });

        if (res.ok) {
            const newComment = await res.json();
            dispatch(createComment(newComment));
            return newComment;
        }
    } catch (err) {
        const errors = err.json();
        return errors;
    }
};

export const getSingleCommentThunk = (commentId) => async (dispatch) => {
    try {
        const res = await fetch(`/api/comments/${commentId}`);

        if (res.ok) {
            const singleComment = await res.json();
            dispatch(getSingleComment(singleComment));
            return singleComment;
        }
    } catch (err) {
        // console.log(err)
        const errors = err.json();
        return errors;
    }
};


const initialState = { imageComments: {}, userComments: {}, singleComment:{} };

const commentReducer = (state = initialState, action) => {
    let newState = {};
    switch (action.type) {
        case GET_ALL_COMMENTS: {
            newState = { ...state, allComments: {} };
            action.comments.comments.forEach((comment) => {
                newState.allImages[comment.id] = comment;
            });
            return newState;
        }
        case CREATE_COMMENT:
            newState = { ...state, imageComments: { ...state.imageComments }, userComments: { ...state.userComments } }
            newState.imageComments[action.comment.id] = action.comment
            return newState
        case UPDATE_COMMENT:
            newState = newState = { ...state, singleComment: { ...state.singleComment }}
            return { ...state, singleComment: { ...action.comment } }
        case DELETE_COMMENT:
            newState = { ...state, imageComments: { ...state.imageComments }, userComments: {} }
            delete newState.imageComments[action.comment.id]
            return newState;
        case GET_SINGLE_COMMENT: {
            newState = { ...state, singleComment: { ...state.singleComment } };
            newState.singleComment = action.comment;
            return newState;
        }
        default:
            return state;
    }

}

export default commentReducer
