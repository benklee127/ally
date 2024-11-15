const GET_USER_COLLECTIONS = "collection/GET_USER_COLLECTIONS";
const CREATE_COLLECTION = "collection/CREATE_COLLECTION";
const UPDATE_COLLECTION = "collection/UPDATE_COLLECTION";
const DELETE_COLLECTION = "collection/DELETE_COLLECTION";
const LOAD_COLLECTION = "collection/LOAD_COLLECTION";

const getUserCollections = (collections) => ({
    type: GET_USER_COLLECTIONS,
    collections,
});

const loadCollectionAction = (collection) => ({
  type: LOAD_COLLECTION,
  collection,
})

const createCollection = (collection) => ({
    type: CREATE_COLLECTION,
    collection,
});

const updateCollectionAction = (collection) => ({
    type: UPDATE_COLLECTION,
    collection,
});

const deleteCollection = (collection) => ({
    type: DELETE_COLLECTION,
    collection,
});

export const getUserCollectionsThunk = () => async (dispatch) => {
    const res = await fetch(`/api/datasets`)

    if (res.ok){
        console.log('res ok');
        const {collections} = await res.json();
        console.log('collections', collections);
        dispatch(getUserCollections(collections))
        return collections;
    }
}

export const loadCollectionThunk = (collectionId) => async(dispatch) => {
  const res = await fetch(`/api/datasets/${collectionId}`)

  if (res.ok) {
    console.log('res ok')
    const collection = await res.json();
    console.log('collection loaded,', collection)
    dispatch (loadCollectionAction(collection))
    return collection
  }
}

export const updateCollectionThunk = (collection, collection_id) => async(dispatch) => {
  const res = await fetch (`/api/datasets/update/${collection_id}`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(collection),
  });

  if (res.ok) {
    const update_collection = await res.json();

    dispatch(updateCollectionAction(update_collection));
    
  }
}

const initialState = {
    collections: [], 
    currCollection: null
  };

const collectionReducer = (state = initialState, action) => {
    switch (action.type) {
      case GET_USER_COLLECTIONS:
        console.log('in reducer, action.collections', action.collections);
        return {
          ...state,
          collections: action.collections
        };
      case LOAD_COLLECTION: {
        console.log('loading collection by id')
        const newState = {...state};
        newState.currCollection = action.collection
        return newState
      }
      case UPDATE_COLLECTION: {
        const newState = {...state};
        newState.currCollection = action.collection
        return newState
      } 
      
        
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
