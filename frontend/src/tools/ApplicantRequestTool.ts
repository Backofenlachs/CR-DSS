
import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js";
import type { ScoringModelVersion, ApplicantRequestDataV010, ApplicantRequestDataV020 } from "../services/RiskAssessmentService.js";
import { RiskAssessmentStore } from "../stores/RiskAssessmentStore.js";

import { ApplicantRequestView } from "./ApplicantRequestView.js";


export class ApplicantRequestTool extends BaseTool {

    private readonly view = new ApplicantRequestView();

    // Local UI state
    private selectedScoringModel: ScoringModelVersion | null = null;
    
    override render($root: UiEngineRoot): void {
        super.render($root);

        // Render UI
        $root.html(this.view.render());

        // Find ui elements
        const $form = $root.find('#applicant-request-form');
        const $select = $form.find('#scoring-model');
        

        if ($select.length !== 1 || $form.length !== 1) {
            throw new Error("[ApplicantRequestTool] Required UI elements not found");
        }

        // Bind event: scoring-model selection on change
        $select.on('change', (event: Event) => {
            const select = event.currentTarget as HTMLSelectElement;
            const value = select.value;

            
            const model: ScoringModelVersion | null =
                value === 'v0.1.0' || value === 'v0.2.0' ? value : null;
                    
            
            this.selectedScoringModel = model;

            // Hide all sections
            $root.find('[data-scoring-version]').prop('hidden', true);

            // Show selected section or fallback
            $root.find(`[data-scoring-version="${model ?? '---'}"]`).prop('hidden', false)
        });


        // Bind event: form 
        $form.on('submit', async (event: Event) => {
            event.preventDefault();

            const form = event.currentTarget;

            if (!(form instanceof HTMLFormElement)) return;
            if (this.selectedScoringModel === null) return;

            const formData = new FormData(form);

            switch(this.selectedScoringModel) {
                case 'v0.1.0': {
                    const applicantData: ApplicantRequestDataV010 = {
                        scoring_model: 'v0.1.0',
                        
                        monthly_net_income: Number(formData.get("monthly_net_income")),
                        existing_monthly_debt_payments: Number(formData.get("existing_monthly_debt_payments")),
                        monthly_fixed_costs: Number(formData.get("monthly_fixed_costs")),

                        loan_amount: Number(formData.get("loan_amount")),
                        annual_interest_rate: Number(formData.get("annual_interest_rate")),
                        loan_term_months: Number(formData.get("loan_term_months"))
                    }

                    await RiskAssessmentStore.evaluate(applicantData);
                    break;
                }

                case 'v0.2.0': {
                    const applicantData: ApplicantRequestDataV020 = {
                        scoring_model: 'v0.2.0',

                        monthly_net_income: Number(formData.get("monthly_net_income")),
                        existing_monthly_debt_payments: Number(formData.get("existing_monthly_debt_payments")),
                        monthly_fixed_costs: Number(formData.get("monthly_fixed_costs")),
                        cash_reserve: Number(formData.get("cash_reserve")),
                        employment_months: Number(formData.get("employment_months")),
                        age: Number(formData.get("age")),

                        loan_amount: Number(formData.get("loan_amount")),
                        annual_interest_rate: Number(formData.get("annual_interest_rate")),
                        loan_term_months: Number(formData.get("loan_term_months"))
                    }

                    await RiskAssessmentStore.evaluate(applicantData);
                    break;
                }

                default:
                    console.warn('[ApplicantRequestTool] No scoring model selected');
                    return;
            }
        });
    }
    
    override destroy(): void {
        

        //this.controller.destroy();
        //this.form = null;

        super.destroy();
    }
}
