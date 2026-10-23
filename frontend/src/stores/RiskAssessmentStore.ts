import {
    RiskAssessmentService,
    type ApplicantRequestDataV010,
    type ApplicantRequestDataV020,
    type RiskAssessmentResult
} from "../services/RiskAssessmentService.js";

export type StoreStates = 'empty' | 'loading' | 'idle';

export const RESULT_EVENT_KEY = 'update-result'
let result: RiskAssessmentResult | null = null;

export const STATE_EVENT_KEY = 'update-state';
let state: StoreStates = 'empty'  

const events = new EventTarget();

function setState(newState: StoreStates): void {
    if (state === newState) return;

    state = newState;

    events.dispatchEvent(
        new CustomEvent(STATE_EVENT_KEY, { detail: state})
    )
}

function setResult(newResult: RiskAssessmentResult): void {
    result = newResult;

    events.dispatchEvent(new CustomEvent(RESULT_EVENT_KEY, { detail: newResult }));
}

export const RiskAssessmentStore = {


    async evaluate(applicantData: ApplicantRequestDataV010 | ApplicantRequestDataV020): Promise<void> {
        setState('loading');

        try {
            const response = await RiskAssessmentService.evaluate(applicantData);

            await new Promise(resolve => setTimeout(resolve, 1000));

            setResult(response.data);   
        } finally {
            setState(result ? 'idle' : 'empty')
        }
    },

    getState(): StoreStates {
        return state;
    },

    addEventListener(type: string, listener: EventListener): void {
        events.addEventListener(type, listener);
    },

    removeEventListener(type: string, listener: EventListener): void {
        events.removeEventListener(type, listener);
    }
};