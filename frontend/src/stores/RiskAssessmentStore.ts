import {
    RiskAssessmentService,
    type ApplicantRequestData,
    type RiskAssessmentResult
} from "../services/RiskAssessmentService.js";


export const RESULT_EVENT_KEY = 'update-result'
let result: RiskAssessmentResult | null = null;


const events = new EventTarget();
function setResult(newResult: RiskAssessmentResult): void {
    result = newResult;

    events.dispatchEvent(new CustomEvent(RESULT_EVENT_KEY, { detail: newResult }));
}

export const RiskAssessmentStore = {


    async evaluate(applicantData: ApplicantRequestData): Promise<void> {

        const response = await RiskAssessmentService.evaluate(applicantData);

        setResult(response.data);
    },


    addEventListener(type: string, listener: EventListener): void {
        events.addEventListener(type, listener);
    },

    removeEventListener(type: string, listener: EventListener): void {
        events.removeEventListener(type, listener);
    }
};