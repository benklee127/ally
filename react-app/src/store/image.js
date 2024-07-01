// import { csrfFetch } from "./csrf";

//type string

const GET_ALL_IMAGES = "image/GET_ALL_IMAGES";
const CREATE_IMAGE = "image/CREATE_IMAGE";
const UPDATE_IMAGE = "image/UPDATE_IMAGE";
const DELETE_IMAGE = "image/DELETE_IMAGE";
const GET_USER_IMAGES = "image/GET_USER_IMAGES";
const GET_SINGLE_IMAGE = "image/GET_SINGLE_IMAGE";
const GET_IMAGE_COMMENTS = "image/GET_IMAGE_COMMENTS";
const GET_USER_FAV_IMG = "image/GET_USER_FAV_IMG";
const ADD_USER_FAV_IMG = "image/ADD_USER_FAV_IMG";
const DELETE_USER_FAV_IMG = "image/DELETE_USER_FAV_IMG";
const GET_ALL_FAV_IMG = "image/GET_ALL_FAV_IMG";

//action creator
const getAllImages = (images) => ({
  type: GET_ALL_IMAGES,
  images,
});

const createImage = (image) => ({
  type: CREATE_IMAGE,
  image,
});

const updateImage = (image) => ({
  type: UPDATE_IMAGE,
  image,
});

const deleteImage = (image_id) => ({
  type: DELETE_IMAGE,
  image_id,
});

const getUserImages = (images) => ({
  type: GET_USER_IMAGES,
  images,
});

const getSingleImage = (image) => ({
  type: GET_SINGLE_IMAGE,
  image,
});

const getImageComments = (image) => ({
  type: GET_IMAGE_COMMENTS,
  image,
});

const getUserFavImg = (images) => ({
  type: GET_USER_FAV_IMG,
  images,
});

const addUserFavImg = (image) => ({
  type: ADD_USER_FAV_IMG,
  image,
});

const deleteUserFavImg = (image_id) => ({
  type: DELETE_USER_FAV_IMG,
  image_id,
});

const getAllFavImg = (images) => ({
  type: GET_ALL_FAV_IMG,
  images,
});

//thunk
export const getAllImageThunk = () => async (dispatch) => {
  try {
    const res = await fetch("/api/images");

    if (res.ok) {
      const images = await res.json();
      dispatch(getAllImages(images));
      return images;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const createImageThunk = (image, user) => async (dispatch) => {
  // console.log("userId in create image", user.id);
  // console.log("image  in create image", image);
  const res = await fetch(`/api/images/${user.id}/images`, {
    method: "POST",
    // headers: { "Content-Type": "application/json" },
    // body: JSON.stringify(image),
    body: image,
  });

  // console.log("res in the CREATIMGAEJ:JDK:JSDKJ;", res);

  if (res.ok) {
    // const newImage = await res.json();
    const { resImage } = await res.json();
    dispatch(createImage(resImage));
    return resImage;
  } else if (res.status < 500) {
    // console.log("image route error");
    const data = await res.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

export const updateImageThunk = (image, imageId) => async (dispatch) => {
  // console.log(" in the update image thunk!!!!!");
  try {
    const res = await fetch(`/api/images/${imageId}/update`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(image),
    });

    // console.log("Res in the updateimagethunk::", res);

    if (res.ok) {
      // console.log("update image in the upated thunk~~~~");
      const updatedImage = await res.json();
      // console.log("updateImage in the res.ok: ", updatedImage);
      dispatch(updateImage(updatedImage));

      return updatedImage;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const deleteImageThunk = (image_id) => async (dispatch) => {
  try {
    const res = await fetch(`/api/images/delete/${image_id}`, {
      method: "GET",
    });

    if (res.ok) {
      dispatch(deleteImage(image_id));
      return;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const getUserImagesThunk = (user_id) => async (dispatch) => {
  try {
    // console.log("userimages user Id", user_id);

    const res = await fetch(`/api/images/user/${user_id}`);

    if (res.ok) {
      const userImages = await res.json();
      dispatch(getUserImages(userImages));
      return userImages;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const getSingleImageThunk = (imageId) => async (dispatch) => {
  // console.log("single image in thunk!!!!!");
  try {
    const res = await fetch(`/api/images/${imageId}`);

    if (res.ok) {
      const singleImage = await res.json();
      dispatch(getSingleImage(singleImage));
      return singleImage;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const getImageCommentsThunk = (image_id) => async (dispatch) => {
  try {
    const res = await fetch(`/api/images/${image_id}/comments`);

    if (res.ok) {
      const imageComments = await res.json();
      dispatch(getImageComments(imageComments));
      return imageComments;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const getUserFavImgThunk = (userId) => async (dispatch) => {
  // console.log("getuserfavimg in the Thunk!!!")

  try {
    const res = await fetch(`/api/images/${userId}/user_favorite`);

    if (res.ok) {
      // console.log("res return if res is OK: ", res)
      const userFavImgs = await res.json();
      // console.log("userFavImgs in res.ok: ", userFavImgs)
      dispatch(getUserFavImg(userFavImgs));
      return userFavImgs;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const addUserFavThunk = (image) => async (dispatch) => {
  // console.log("In the adduserFav thunk!!!!");
  try {
    // console.log("request body: ", JSON.stringify(image));
    const res = fetch("/api/images/user_favorite", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(image),
    });

    // console.log("after res !!!!!!!!!", res);

    if (res.ok) {
      const newFavImg = await res.json();
      // console.log("res in the add user fav!!!", res);
      dispatch(addUserFavImg(newFavImg));
      return newFavImg;
    }
  } catch (err) {
    const errors = err.json();
    return errors;
  }
};

export const deleteUserFavImgThunk = (userId, imageId) => async (dispatch) => {
  // console.log("in deleteUserFavImgThunk~~~~")
  try {
    const res = await fetch(
      `/api/images/delete/${userId}/user_favorite/${imageId}`,
      {
        method: "GET",
      }
    );

    if (res.ok) {
      dispatch(deleteUserFavImg(imageId));
      return;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};

export const getAllFavImguserThunk = (imageId) => async (dispatch) => {
  // console.log("in the getallfavimguserthunk~~~~");
  try {
    const res = await fetch(`/api/images/favorites/${imageId}/all`);

    if (res.ok) {
      // console.log("res in teh getallfavimguserthunk: ", res);
      const allFavImgs = await res.json();
      // console.log("allfavimgs in the res.ok : ", allFavImgs);
      dispatch(getAllFavImg(allFavImgs));
      return allFavImgs;
    }
  } catch (err) {
    const errors = await err.json();
    return errors;
  }
};
//reducer function

const initialState = {
  allImages: {},
  userImages: {},
  singleImage: {},
  imageComments: {},
  userFavImg: {},
  allFavImgUser: {},
};

const imageReducer = (state = initialState, action) => {
  let newState = {};
  // console.log("Image state in reducer function: ", action, state);

  switch (action.type) {
    case GET_ALL_IMAGES: {
      newState = { ...state, allImages: {} };
      action.images.images.forEach((image) => {
        newState.allImages[image.id] = image;
      });
      return newState;
    }
    case CREATE_IMAGE: {
      newState = { ...state, userImages: { ...state.userImages } };
      newState.singleImage = action.image;
      return newState;
    }
    case UPDATE_IMAGE: {
      // newState = { ...state, singleImage: { ...state.singleImage } };
      // newState = { ...state, singleImage: {} };
      // console.log("Update image in the reducer function~~~~~");
      newState = { ...state, allImages: { ...state.allImages } };
      newState.allImages[action.image.id] = action.image;
      return newState;
    }
    case DELETE_IMAGE: {
      newState = { ...state, userImages: { ...state.userImages } };
      delete newState.userImages[action.image_id];
      return newState;
    }
    case GET_USER_IMAGES: {
      newState = { ...state, userImages: { ...state.userImages } };
      newState.userImages = action.images;
      return newState;
    }
    case GET_SINGLE_IMAGE: {
      newState = { ...state, singleImage: { ...state.singleImage } };
      newState.singleImage = action.image;
      return newState;
    }
    case GET_IMAGE_COMMENTS: {
      newState = { ...state, imageComments: {} };
      action.image.comments.forEach((comment) => {
        newState.imageComments[comment.id] = comment;
      });
      return newState;
    }
    case GET_USER_FAV_IMG: {
      newState = { ...state, userFavImg: {} };
      action.images.forEach((image) => {
        newState.userFavImg[image.id] = image;
      });
      return newState;
    }
    case ADD_USER_FAV_IMG: {
      const newState = { ...state, userFavImg: { ...state.userFavImg } };
      newState.userFavImg[action.image.id] = action.image;
      return newState;
    }
    case DELETE_USER_FAV_IMG: {
      const newState = { ...state, userFavImg: { ...state.userFavImg } };
      delete newState.userFavImg[action.image_id];
      return newState;
    }
    case GET_ALL_FAV_IMG: {
      const newState = { ...state, allFavImgUser: {} };
      // console.log("action images in the reducer function: ", action.images)
      action.images.forEach((image) => {
        newState.allFavImgUser[image.id] = image;
      });
      return newState;
    }
    default:
      return state;
  }
};

export default imageReducer;
