
import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js";

import { ApplicantRequestController } from "./ApplicantRequestController.js";
import { ApplicantRequestView } from "./ApplicantRequestView.js";

export type ScoringModel = 'v0.1.0' | 'v0.2.0';

export class ApplicantRequestTool extends BaseTool {

    private readonly controller = new ApplicantRequestController();
    private readonly view = new ApplicantRequestView();

    // Local UI state
    private selectedScoringModel: ScoringModel | null = null;
    
    override render($root: UiEngineRoot): void {
        super.render($root);

        // Render UI
        $root.html(this.view.render());

        // Find scoring model selector
        const select = $root.find('#scoring-model');

        if (select.length !== 1) {
            throw new Error("[ApplicantRequestTool] Scoring model selector not found");
        }

        // Bind event: scoring-model selection on change
        $root.find('#scoring-model').on('change', (event: Event) => {
            const select = event.currentTarget as HTMLSelectElement;
            const value = select.value;

            // Validate selected model
            const model: ScoringModel | null =
                value === 'v0.1.0' || value === 'v0.2.0' ? value : null;
                    
            // Update local state
            this.selectedScoringModel = model;

            // Hide all sections
            $root.find('[data-scoring-version]').prop('hidden', true);

            // Show selected section or fallback
            $root.find(`[data-scoring-version="${model ?? '---'}"]`).prop('hidden', false)
        });


        // legacy: bind submit button
        const form = document.getElementById("applicant-request-form");

        if (!(form instanceof HTMLFormElement)) {
            throw new Error("[ApplicantRequestTool] Applicant request form not found")
        }

        //this.controller.bind(form);
    }
    
    override destroy(): void {
        

        this.controller.destroy();
        //this.form = null;

        super.destroy();
    }
}
