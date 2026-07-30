import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js";

export class ApplicantRequestTool extends BaseTool {

    override render($root: UiEngineRoot): void {
        super.render($root);

        const html = /*html*/ `
            <section
                class="applicant-request"
                aria-labelledby="applicant-request-title"
            >
                <header class="applicant-request__header">
                    <h1
                        id="applicant-request-title"
                        class="applicant-request__title"
                    >
                        Applicant / Request
                    </h1>

                    <p class="applicant-request__description">
                        Enter the applicant and loan request data.
                    </p>
                </header>

                <form class="applicant-request__form">
                    <fieldset class="applicant-request__section">
                        <legend class="applicant-request__section-title">
                            Application
                        </legend>

                        <div class="applicant-request__fields">
                            <!-- Application number -->
                            <!-- Scoring model -->
                        </div>
                    </fieldset>

                    <fieldset class="applicant-request__section">
                        <legend class="applicant-request__section-title">
                            Applicant
                        </legend>

                        <div class="applicant-request__fields">
                            <!-- Age -->
                            <!-- Employment months -->
                        </div>
                    </fieldset>

                    <fieldset class="applicant-request__section">
                        <legend class="applicant-request__section-title">
                            Financial situation
                        </legend>

                        <div class="applicant-request__fields">
                            <!-- Monthly net income -->
                            <!-- Monthly fixed costs -->
                            <!-- Existing debt payments -->
                            <!-- Cash reserve -->
                        </div>
                    </fieldset>

                    <fieldset class="applicant-request__section">
                        <legend class="applicant-request__section-title">
                            Loan request
                        </legend>

                        <div class="applicant-request__fields">
                            <!-- Loan amount -->
                            <!-- Annual interest rate -->
                            <!-- Loan term -->
                        </div>
                    </fieldset>

                    <footer class="applicant-request__actions">
                        <button
                            class="applicant-request__submit"
                            type="submit"
                        >
                            Evaluate application
                        </button>
                    </footer>
                </form>
            </section>
        `;

        $root.html(html);
    }
}