import { RiskAssessmentStore } from "../stores/RiskAssessmentStore.js";

import type { ApplicantRequestData } from "../services/RiskAssessmentService.js";



export class ApplicantRequestController {

    private form: HTMLFormElement | null = null;


    bind(form: HTMLFormElement): void {
        this.form = form;

        this.form.addEventListener(
            "submit",
            this.handleSubmit
        );
    }


    destroy(): void {
        this.form?.removeEventListener(
            "submit",
            this.handleSubmit
        );

        this.form = null;
    }


    private handleSubmit = async (
        event: SubmitEvent
    ): Promise<void> => {

        event.preventDefault();

        if (!this.form) {
            return;
        }

        const formData = new FormData(this.form);

        const applicantData: ApplicantRequestData = {
            scoring_model:
                String(formData.get("scoring_model")),

            age: Number(formData.get("age")),
            employment_months: Number(formData.get("employment_months")),
            monthly_net_income: Number(formData.get("monthly_net_income")),
            monthly_fixed_costs: Number(formData.get("monthly_fixed_costs")),
            existing_monthly_debt_payments:
                Number(
                    formData.get(
                        "existing_monthly_debt_payments"
                    )
                ),

            cash_reserve:
                Number(formData.get("cash_reserve")),

            loan_amount:
                Number(formData.get("loan_amount")),

            annual_interest_rate:
                Number(formData.get("annual_interest_rate")),

            loan_term_months:
                Number(formData.get("loan_term_months"))
        };
        
        await RiskAssessmentStore.evaluate( applicantData );
    };
}