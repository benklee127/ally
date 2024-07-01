const GET_USER_COLLECTIONS = "collection/GET_USER_COLLECTIONS";
const CREATE_COLLECTION = "collection/CREATE_COLLECTION";
const UPDATE_COLLECTION = "collection/UPDATE_COLLECTION";
const DELETE_COLLECTION = "collection/DELETE_COLLECTION";
const LOAD_COLLECTION = "collection/LOAD_COLLECTION";

const getUserCollections = (collections) => ({
    type: GET_USER_COLLECTIONS,
    collections,
});

const createCollection = (collection) => ({
    type: CREATE_COLLECTION,
    collection,
});

const updateCollection = (collection) => ({
    type: UPDATE_COLLECTION,
    collection,
});

const deleteCollection = (collection) => ({
    type: DELETE_COLLECTION,
    collection,
});

export const getUserCollectionsThunk = () => async (dispatch) => {
    return
    const res = await fetch(`/api/users/collections`)

    if (res.ok){
        console.log('res ok');
        const {collections} = await res.json();
        console.log('collections', collections);
        dispatch(getUserCollections(collections))
        return collections;
    }
}

const initialState = {
    collections: []
  };

const collectionReducer = (state = initialState, action) => {
    switch (action.type) {
      case GET_USER_COLLECTIONS:
        console.log('in reducer, action.collections', action.collections);
        return {
          ...state,
          collections: action.collections
        };
    //   case CREATE_COLLECTION:
    //     return {
    //       ...state,
    //       collections: [...state.collections, action.collection]
    //     };
    //   case UPDATE_COLLECTION:
    //     return {
    //       ...state,
    //       collections: state.collections.map((collection) =>
    //         collection.id === action.collection.id
    //           ? action.collection
    //           : collection
    //       )
    //     };
    //   case DELETE_COLLECTION:
    //     return {
    //       ...state,
    //       collections: state.collections.filter(
    //         (collection) => collection.id !== action.collection.id
    //       )
    //     };
      default:
        return state;
    }
  };

  export default collectionReducer;
