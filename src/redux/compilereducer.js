import { COMPILE, GET_ERRORS} from './types';

const initialState = {
    ratings: [],
    rankings: [],
    avr: [],
    teams:[]
};


const reducer = (state = initialState, action) => {
    switch(action.type) {
        case COMPILE:
            console.log("getting items");
            return {
                ratings: action.payload.ratings,
                avr: action.payload.avr,
                rankings: action.payload.rankings,
                teams: action.payload.teams,
            }
        case GET_ERRORS:
            console.log("errored");
            return state;
        default:
            console.log("defaulted");
            return state;
    }
}

export default reducer;