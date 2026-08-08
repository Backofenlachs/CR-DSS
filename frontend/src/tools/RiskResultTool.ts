import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js";

export class RiskResultTool extends BaseTool {

    override render($root: UiEngineRoot): void {
        super.render($root);

        const html = /*html*/ `
            <section
                class="risk-assessment"
                aria-labelledby="risk-assessment-title"
            >
                <header class="risk-assessment__header">
                    <h1
                        id="risk-assessment-title"
                        class="risk-assessment__title"
                    >
                        Risk Assessment / Result
                    </h1>

                    <p class="risk-assessment__description">
                        Scoring model 0.2.0 - calculated just now
                    </p>
                </header>


                <!-- Decision -->
                <section
                    class="risk-assessment__decision"
                    aria-labelledby="risk-decision-title"
                >
                    <div class="risk-assessment__decision-result">
                        <h2
                            id="risk-decision-title"
                            class="risk-assessment__section-title"
                        >
                            Decision
                        </h2>

                        <strong class="risk-assessment__decision-value">
                            APPROVED
                        </strong>
                    </div>

                    <div class="risk-assessment__score">
                        <span class="risk-assessment__score-label">
                            Risk score
                        </span>

                        <strong class="risk-assessment__score-value">
                            10
                        </strong>
                    </div>
                </section>


                <!-- Calculated metrics -->
                <section
                    class="risk-assessment__metrics"
                    aria-label="Calculated risk metrics"
                >
                    <article class="risk-assessment__metric">
                        <span class="risk-assessment__metric-label">
                            Reserve coverage
                        </span>

                        <strong class="risk-assessment__metric-value">
                            9.4 months
                        </strong>
                    </article>

                    <article class="risk-assessment__metric">
                        <span class="risk-assessment__metric-label">
                            Total DTI
                        </span>

                        <strong class="risk-assessment__metric-value">
                            14.2 %
                        </strong>
                    </article>

                    <article class="risk-assessment__metric">
                        <span class="risk-assessment__metric-label">
                            Residual income
                        </span>

                        <strong class="risk-assessment__metric-value">
                            1,909.49 EUR
                        </strong>
                    </article>

                    <article class="risk-assessment__metric">
                        <span class="risk-assessment__metric-label">
                            Monthly annuity
                        </span>

                        <strong class="risk-assessment__metric-value">
                            360.51 EUR
                        </strong>
                    </article>
                </section>


                <!-- Summary -->
                <section
                    class="risk-assessment__summary"
                    aria-labelledby="risk-summary-title"
                >
                    <h2
                        id="risk-summary-title"
                        class="risk-assessment__summary-title"
                    >
                        Summary record
                    </h2>

                    <p class="risk-assessment__summary-text">
                        The application satisfies the requirements of the
                        selected scoring model. Relevant calculated metrics
                        remain within the configured assessment thresholds.
                    </p>
                </section>
            </section>
        `;
        
        $root.html(html);
    }
}