/**
 * Concept: Reactive UI Lifecycle
 *
 * Status: API Sketch / Not Implemented
 *
 * Idea:
 * - init() constructs the UI once.
 * - UI elements expose direct event bindings.
 * - Local state changes update the existing UI.
 * - render() only mounts the prepared UI tree.
 * - destroy() cleans up resources.
 *
 * This file demonstrates the intended API usage,
 * not a working implementation.
 */


import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js";

import { ApplicantRequestController } from "./ApplicantRequestController.js";
import { ApplicantRequestView } from "./ApplicantRequestView.js";

export type ScoringModel = 'v0.1.0' | 'v0.2.0';

export class ApplicantRequestTool extends BaseTool {

    private readonly controller = new ApplicantRequestController();
    private readonly view = new ApplicantRequestView();

    // Local UI states
    private selectedScoringModel: ScoringModel = 'v0.2.0'

    private ui!: ApplicantRequestUI;

    override init(config?: unknown, runtime?: unknown): void {
        super.init(config, runtime);

        // build the UI once
        this.ui = this.view.createUI();        
        
        // initialize UI state
        this.view.setScoringModel(
            this.ui,
            this.selectedScoringModel
        );

        // Bind local UI events
        this.ui.modelSelector.addEventListener(
            "change",
            this.handleModelChange
        );

        this.controller.bind(this.ui.form);
    }

    override render($root: UiEngineRoot): void {
        super.render($root);

        // mount on existing tree
        // requires an propriate uiengineroot api
        $root.html(this.ui.root);
    }

    override destroy(): void {
        this.controller.destroy();
        super.destroy()
    }

    private handleModelChange = (): void => {
        const model = this.ui.modelSelector.value;

        if (model !== 'v0.1.0' && model !== 'v0.2.0') {
            return;
        }

        this.selectedScoringModel = model;

        this.view.setScoringModel(this.ui, model);
    }


}