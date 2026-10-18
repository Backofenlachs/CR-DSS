export class ApplicantRequestFormV010 {
    public render(): string {
        return /*html*/ `

            <!-- FINANCIAL INFORMATION -->
            <section class="applicant-request__section">
                <h2 class="applicant-request__section-title">
                    Financial situation
                </h2>

                <div class="applicant-request__fields">
                    <!-- Monthly net income -->
                    <div class="applicant-request__field">
                        <label for="monthly-net-income">
                            Monthly net income
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="monthly-net-income"
                                name="monthly_net_income"
                                type="number"
                                min="0"
                                step="0.01"
                                placeholder="3800.00"
                                aria-describedby="monthly-net-income-hint"
                                ><!--required
                            -->

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="monthly-net-income-hint"
                            class="applicant-request__hint"
                        >
                            Applicant's regular monthly income after taxes.
                        </small>
                    </div>

                    <!-- Monthly fixed costs -->
                    <div class="applicant-request__field">
                        <label for="monthly-fixed-costs">
                            Monthly fixed costs
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="monthly-fixed-costs"
                                name="monthly_fixed_costs"
                                type="number"
                                min="0"
                                step="0.01"
                                placeholder="1350.00"
                                aria-describedby="monthly-fixed-costs-hint"
                                ><!--required
                            -->

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="monthly-fixed-costs-hint"
                            class="applicant-request__hint"
                        >
                            Recurring living costs excluding debt payments.
                        </small>
                    </div>

                    <!-- Existing monthly debt payments -->
                    <div class="applicant-request__field">
                        <label for="existing-debt-payments">
                            Existing debt payments
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="existing-debt-payments"
                                name="existing_monthly_debt_payments"
                                type="number"
                                min="0"
                                step="0.01"
                                placeholder="180.00"
                                aria-describedby="existing-debt-payments-hint"
                                ><!--required
                            -->

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="existing-debt-payments-hint"
                            class="applicant-request__hint"
                        >
                            Total monthly payments for existing credit obligations.
                        </small>
                    </div>
                </div>
            </section>

            <!-- REQUESTED LOAN -->
            <section class="applicant-request__section">
                <h2 class="applicant-request__section-title">
                    Loan request
                </h2>

                <div class="applicant-request__fields">
                    <!-- Loan amount -->
                    <div class="applicant-request__field">
                        <label for="loan-amount">
                            Loan amount
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="loan-amount"
                                name="loan_amount"
                                type="number"
                                min="0.01"
                                step="0.01"
                                placeholder="12000.00"
                                aria-describedby="loan-amount-hint"
                                ><!--required
                            -->

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="loan-amount-hint"
                            class="applicant-request__hint"
                        >
                            Principal amount requested by the applicant.
                        </small>
                    </div>

                    <!-- Annual interest rate -->
                    <div class="applicant-request__field">
                        <label for="annual-interest-rate">
                            Annual interest rate
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="annual-interest-rate"
                                name="annual_interest_rate"
                                type="number"
                                min="0"
                                max="100"
                                step="0.01"
                                placeholder="5.20"
                                aria-describedby="annual-interest-rate-hint"
                                ><!--required
                            -->

                            <span class="applicant-request__input-unit">
                                %
                            </span>
                        </div>

                        <small
                            id="annual-interest-rate-hint"
                            class="applicant-request__hint"
                        >
                            Nominal annual interest rate in percent.
                        </small>
                    </div>

                    <!-- Loan term months-->
                    <div class="applicant-request__field">
                        <label for="loan-term-months">
                            Loan term
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="loan-term-months"
                                name="loan_term_months"
                                type="number"
                                min="1"
                                step="1"
                                placeholder="36"
                                aria-describedby="loan-term-months-hint"
                                ><!--required
                            -->

                            <span class="applicant-request__input-unit">
                                months
                            </span>
                        </div>

                        <small
                            id="loan-term-months-hint"
                            class="applicant-request__hint"
                        >
                            Requested repayment period in full months.
                        </small>
                    </div>
                </div>
            </section>
        `

    }
}