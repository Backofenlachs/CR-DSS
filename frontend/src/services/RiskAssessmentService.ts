import '../types/Api.js'
import type ApiResponse from '../types/Api.js';

export interface ApplicantRequestData {
    scoring_model: string;

    age: number;
    employment_months: number;

    monthly_net_income: number;
    monthly_fixed_costs: number;
    existing_monthly_debt_payments: number;
    cash_reserve: number;

    loan_amount: number;
    annual_interest_rate: number;
    loan_term_months: number;
}

export interface RiskAssessmentResult {
    applicant_number: string;
    result: string
}

const RISK_ASSESSMENT_ENDPOINT = "/api/risk-assessment"


export const RiskAssessmentService = {
    async evaluate(applicantData: ApplicantRequestData): Promise<ApiResponse<RiskAssessmentResult>> {
        
        const response = await fetch( RISK_ASSESSMENT_ENDPOINT, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(applicantData)
        });

        if (!response.ok) {
            throw new Error(`[RiskAssessmentService.evaluate] Request failed: HTTP ${response.status}`)
        }


        const data = (await response.json()) as ApiResponse<RiskAssessmentResult>

        return data;

    }

}


// ================== Dummy Data =====================

const dummyApplicantData: ApplicantRequestData = {
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
    result: "approved"
};