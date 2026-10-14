import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js";

import { ApplicantRequestController } from "./ApplicantRequestController.js";
import { ApplicantRequestView } from "./ApplicantRequestView.js";

export type ScoringModel = 'v0.1.0' | 'v0.2.0';

export class ApplicantRequestTool extends BaseTool {

    private readonly controller = new ApplicantRequestController();
    private readonly view = new ApplicantRequestView();

    // Local UI states
    private selectedScoringModel: ScoringModel = 'v0.2.0'

    override render($root: UiEngineRoot): void {
        super.render($root);


        $root.html(this.view.getForm(this.selectedScoringModel));

        const form = document.getElementById("applicant-request-form");

        if (!(form instanceof HTMLFormElement)) {
            throw new Error("[ApplicantRequestTool] Applicant request form not found")
        }

        this.controller.bind(form);
    }

    override destroy(): void {
        this.controller.destroy();
        super.destroy()
    }
}