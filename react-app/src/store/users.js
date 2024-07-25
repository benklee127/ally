//type string

const ADD_USER_FAV = "users/ADD_USER_FAV";
const GET_USER_INFO = "users/GET_USER_INFO";
const UPDATE_USER_INFO = "users/UPDATE_USER_INFO";
const UPDATE_USER_SHOWCASE = "users/UPDATE_SHOWCASE";
const GET_USER_SHOWCASE = "users/GET_SHOWCASE";
const DELETE_USER = "users/DELETE_USER";
const EDIT_USER_PROFILE_PHOTO = "user/EDIT_USER_PROFILE_PHOTOTS";
const EDIT_USER_COVER_PHOTO = "user/EDIT_USER_PROFILE_PHOTOTS";
const GET_USER_COLLECTIONS = "collection/GET_USER_COLLECTIONS";
const CREATE_COLLECTION = "collection/CREATE_COLLECTION";
const GET_COLLECTION_MESSAGES = "messages/GET_COLLECTION_MESSAGES";
const SEND_QUERY = "query/SEND_QUERY";
const UPLOAD_FILE = "file/UPLOAD_FILE";
//action creator

const getUserCollections = (collections) => ({
  type: GET_USER_COLLECTIONS,
  collections,
})

const createUserCollection = (collection) => ({
  type: CREATE_COLLECTION,
  collection,
})
const addUserFavAction = (fav) => ({
  type: ADD_USER_FAV,
  fav,
});

const getUserInfoAction = (userInfo) => ({
  type: GET_USER_INFO,
  userInfo,
});

const updateUserInfoAction = (userInfo) => ({
  type: UPDATE_USER_INFO,
  userInfo,
});

const updateUserShowcaseAction = (userShowcase) => ({
  type: UPDATE_USER_SHOWCASE,
  userShowcase,
});

const getUserShowcaseAction = (userShowcase) => ({
  type: GET_USER_SHOWCASE,
  userShowcase,
});

const deleteUserAction = () => ({
  type: DELETE_USER,
});

const editUserProfilePhoto = (photo) => ({
  type: EDIT_USER_PROFILE_PHOTO,
  photo,
});

const editUserCoverPhoto = (photo) => ({
  type: EDIT_USER_COVER_PHOTO,
  photo,
});

const getCollectionMessagesAction = (messages) => ({
  type: GET_COLLECTION_MESSAGES,
  messages,
})

const sendQueryAction = (messages) => ({
  type: SEND_QUERY,
  messages,
})

//thunk creator
export const createCollectionThunk = (collection) => async (dispatch) => {
  try {
    const res = await fetch(`/api/users/collections/create`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(collection),
    });
    if (res.ok) {
      const newCollection = await res.json();
      dispatch(createUserCollection(newCollection));

      return newCollection;
    }
  } catch (err) {
    return err;
  }
}
export const updateUserShowcaseThunk =
  (userId, showcaseInputs) => async (dispatch) => {
    // console.log("in update showcase thunk");
    try {
      const res = await fetch(`/api/users/update/showcase`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(showcaseInputs),
      });
      // console.log("update user showcase thunk midpoint");
      if (res.ok) {
        const userShowcase = await res.json();
        dispatch(updateUserShowcaseAction(userShowcase));
      }
    } catch (err) {
      return err;
    }
  };

export const getUserShowcaseThunk = (userId) => async (dispatch) => {
  try {
    const res = await fetch(`/api/users/showcase/${userId}`);

    if (res.ok) {
      const userShowcase = await res.json();
      // console.log("user Showcase in thunk", userShowcase);
      dispatch(getUserShowcaseAction(userShowcase));
      return userId;
    }
  } catch (err) {
    return err;
  }
};

export const updateUserInfoThunk =
  (userInfo, userId, formType) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/details/${formType}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userInfo),
    });

    if (res.ok) {
      let newUserInfo = await res.json();
      // console.log("res.json", newUserInfo);
      dispatch(updateUserInfoAction(newUserInfo));
    } else if (res.status < 500) {
      const data = await res.json();
      if (data.errors) {
        return data.errors;
      }
    } else {
      return ["An error occurred. Please try again."];
    }
  };

export const userInfoThunk = (userId) => async (dispatch) => {
  //   console.log("userinfo thunk called", userId);
  try {
    const res = await fetch(`/api/users/${userId}`);
    if (res.ok) {
      //   console.log("userinfo thunk res ok");
      const userInfo = await res.json();
      //   console.log("userInfo in thunk after res", userInfo);
      dispatch(getUserInfoAction(userInfo));
      return userInfo;
    }
  } catch (err) {
    return err;
  }
};

export const userDeleteThunk = (userId) => async (dispatch) => {
  // console.log("in delete thunk");
  try {
    const res = await fetch(`/api/users/deleteuser/${userId}`);
    if (res.ok) {
      dispatch(deleteUserAction());
    }
  } catch (err) {
    return err;
  }
};

export const editUserProfilePhotoThunk = (photo, userId) => async ( dispatch ) => {

  // console.log("in the edituser profile photo thunk~~~~~~~~~~")
  // console.log("userid in the edit user profilephotothunk: ", userId)
  // console.log("photo in edit user profile thunk: ", photo)
  try {
    // console.log("in the try block of the edituser profilephotothunk!!!!!!!!!!!!!!!")
    const res = await fetch(`/api/users/${userId}/profile_photo`, {
      method : "POST",
      body: photo,
    })

    // console.log("result befor the if res.ok statement: ", res)

    if(res.ok) {
      // console.log("res in the if statement: ", res)
      const newPhoto = await res.json();
      dispatch(editUserProfilePhoto(newPhoto));
      return newPhoto;
    }
  }
  catch(err) {
    const errors = await err.json();
    return errors;
  }
};


export const editUserCoverPhotoThunk = (photo, userId) => async ( dispatch ) => {
  try {
    const res = await fetch(`/api/users/${userId}/cover_photo`, {
      method : "POST",
      body: photo,
    })

    if(res.ok) {
      // console.log("res in the if statement: ", res)
      const newPhoto = await res.json();
      dispatch(editUserCoverPhoto(newPhoto));
      return newPhoto;
    }
  } catch(err) {
    const errors = await err.json();
    return errors;
  }
};
export const getUserCollectionsThunk = () => async (dispatch) => {

  const res = await fetch(`/api/users/collections`)

  if (res.ok){
      console.log('res ok');
      const collections = await res.json();
      console.log('collections', collections);
      dispatch(getUserCollections(collections))
      return collections;
  }
}
export const getCollectionMessagesThunk = (collectionId) => async (dispatch) => {
  const res = await fetch(`/api/messages/${collectionId}`)

  if (res.ok){
    const messages = await res.json();
    dispatch(getCollectionMessagesAction(messages))
    return messages;
  }
}

export const sendQueryThunk = (query, collectionId) => async (dispatch) => {
  const res = await fetch(`/api/query/${collectionId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(query),
  });

  if (res.ok) {
    const messages = await res.json();
    dispatch(getCollectionMessagesAction(messages));
    return messages;
  }
}

const uploadFileAction = (file) => ({
  type: UPLOAD_FILE,
  file
})

export const uploadFileThunk = (newFile, collectionId) => async (dispatch) => {
  console.log("in the upload file thunk", newFile, collectionId)
  const res = await fetch(`/api/upload/${collectionId}`, {
    method: "POST",
    body: newFile
  })
  if (res.ok) {
    const filestatus = await res.json();
    dispatch(uploadFileAction(filestatus))
    return filestatus;
  }
}



//reducer function
const initialState = { userFav: {}, userInfo: {}, userShowcase: {}, userProfilePhoto: false, userCoverPhoto: {}, collections: {}, currCollection: {}, messages: {} , filestatus: ""};

const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_USER_COLLECTIONS:{
      const newState = {...state };
      newState.collections = action.collections.datasets;
      return newState;
    }
    case GET_COLLECTION_MESSAGES:{
      const newState = {...state };
      newState.messages = action.messages.messages;
      return newState;
    }
    case UPLOAD_FILE:{
      const newState = {...state,};
      newState.filestatus = action.file.filestatus;
      return newState;
    }

    // case CREATE_COLLECTION:{
    //   const newState = {...state };
    //   const collections = action.collections.datasets
    //   newState.collections = collections;
    //   newState.currCollection = collections[collections.length-1];
    //   return newState
    // }
    case GET_USER_INFO: {
      // console.log("get user info called");
      const newState = { ...state };
      newState.userInfo = action.userInfo;
      return newState;
    }
    case UPDATE_USER_INFO: {
      const newState = { ...state, userInfo: { ...state.userInfo } };
      newState.userInfo = action.userInfo;
      return newState;
    }
    case GET_USER_SHOWCASE: {
      const newState = { ...state, userShowcase: { ...state.userShowcase } };
      newState.userShowcase = action.userShowcase;
      return newState;
    }
    case DELETE_USER: {
      const newState = {
        ...state,
        userFav: {},
        userInfo: {},
        userShowcase: {},
      };
      newState = newState;
      return newState;
    }
    case UPDATE_USER_SHOWCASE: {
      // console.log(
      //   "in update user showcase reducer usershowcase",
      //   action.userShowcase
      // );
      const newState = {
        ...state,
        userShowcase: { ...state.userShowcase },
      };
      newState.userShowcase = action.userShowcase;
      return newState;
    };
    case EDIT_USER_PROFILE_PHOTO: {
      const newState = { ...state, userProfilePhoto: {...state.userProfilePhoto}};
      newState.userProfilePhoto = action.photo;
      // newState.userInfo = action.photo;
      return newState;
    };
    case EDIT_USER_COVER_PHOTO: {
      const newState = { ...state, userCoverPhoto: {...state.userCoverPhoto}};
      newState.userCoverPhoto = action.photo;
      return newState;
    }
    default:
      return state;
  }
};

export default userReducer;
