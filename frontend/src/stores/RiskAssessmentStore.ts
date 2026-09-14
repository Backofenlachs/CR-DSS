import {
    RiskAssessmentService,
    type ApplicantRequestData
} from "../services/RiskAssessmentService.js";


export const RiskAssessmentStore = {

    async evaluate(
        applicantData: ApplicantRequestData
    ): Promise<void> {

        await RiskAssessmentService.evaluate(applicantData);
    }

};