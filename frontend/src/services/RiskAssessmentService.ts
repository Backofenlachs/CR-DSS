import { ApplicantRequestFormV020 } from '../tools/ApplicantRequestFormV020.js';
import '../types/Api.js'
import type ApiResponse from '../types/Api.js';


export type ScoringModelVersion = 'v0.1.0' | 'v0.2.0';

type ApplicantRequestData<
    T extends object, 
    V extends ScoringModelVersion
> = T & {
    scoring_model: V;
}

interface ScoringInputV010 {
    monthly_net_income: number;
    existing_monthly_debt_payments: number;
    monthly_fixed_costs: number;

    loan_amount: number;
    annual_interest_rate: number;
    loan_term_months: number;
}

interface ScoringInputV020 {
    employment_months: number;
    age: number;
    monthly_net_income: number;
    existing_monthly_debt_payments: number;
    monthly_fixed_costs: number;
    cash_reserve: number;

    loan_amount: number;
    annual_interest_rate: number;
    loan_term_months: number;
}

export type ApplicantRequestDataV010 = ApplicantRequestData<ScoringInputV010, 'v0.1.0'>;
export type ApplicantRequestDataV020 = ApplicantRequestData<ScoringInputV020, 'v0.2.0'>;


export interface RiskAssessmentResult {
    applicant_number: string;
    result: string
}

const RISK_ASSESSMENT_ENDPOINT = "http://localhost:8000/api/risk-assessment"


export const RiskAssessmentService = {
    async evaluate(applicantData: ApplicantRequestDataV010 | ApplicantRequestDataV020): Promise<ApiResponse<RiskAssessmentResult>> {
        console.count("RiskAssessmentService.evaluate -> fetch");
        const response = await fetch(RISK_ASSESSMENT_ENDPOINT, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                data: applicantData 
            })
        });

        if (!response.ok) {
            throw new Error(`[RiskAssessmentService.evaluate] Request failed: HTTP ${response.status}`)
        }


        const data = (await response.json()) as ApiResponse<RiskAssessmentResult>

        return data;

    }

}




// ================== Dummy Data =====================

export const dummyApplicantData: ApplicantRequestDataV020 = {
    scoring_model: "v0.2.0",

    age: 34,
    employment_months: 72,

    monthly_net_income: 3200,
    monthly_fixed_costs: 1450,
    existing_monthly_debt_payments: 250,
    cash_reserve: 12000,

    loan_amount: 25000,
    annual_interest_rate: 5.5,
    loan_term_months: 60
};

const dummyRiskAssessmentResult: RiskAssessmentResult = {
    applicant_number: "APP-0001",
    result: "APPROVED"
};