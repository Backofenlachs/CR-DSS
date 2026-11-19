export class ApplicantRequestFormV020 {
    public render(): string {
        return /*html*/ `
            <!-- APPLICANT INFORMATION -->
            <section class="applicant-request__section">
                <h2 class="applicant-request__section-title">
                    Applicant
                </h2>

                <div class="applicant-request__fields">
                    <!-- Age -->
                    <div class="applicant-request__field">
                        <label for="v020-age">
                            Age
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-age"
                                name="v020-age"
                                type="number"
                                min="18" 
                                step="1"
                                placeholder="35"
                                aria-describedby="age-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                years
                            </span>
                        </div>

                        <small
                            id="age-hint"
                            class="applicant-request__hint"
                        >
                            Applicant's age in completed years.
                        </small>
                    </div>

                    <!-- Employment duration -->
                    <div class="applicant-request__field">
                        <label for="v020-employment-months">
                            Employment duration
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-employment-months"
                                name="v020-employment-months"
                                type="number"
                                min="0"
                                step="1"
                                placeholder="48"
                                aria-describedby="employment-months-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                months
                            </span>
                        </div>

                        <small
                            id="v020-employment-months-hint"
                            class="applicant-request__hint"
                        >
                            Continuous employment with the current employer.
                        </small>
                    </div>
                </div>
            </section>

            <!-- FINANCIAL INFORMATION -->
            <section class="applicant-request__section">
                <h2 class="applicant-request__section-title">
                    Financial situation
                </h2>

                <div class="applicant-request__fields">
                    <!-- Monthly net income -->
                    <div class="applicant-request__field">
                        <label for="v020-monthly-net-income">
                            Monthly net income
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-monthly-net-income"
                                name="v020-monthly-net-income"
                                type="number"
                                min="0.01"
                                step="0.01"
                                placeholder="3800.00"
                                aria-describedby="monthly-net-income-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="v020-monthly-net-income-hint"
                            class="applicant-request__hint"
                        >
                            Applicant's regular monthly income after taxes.
                        </small>
                    </div>

                    <!-- Monthly fixed costs -->
                    <div class="applicant-request__field">
                        <label for="v020-monthly-fixed-costs">
                            Monthly fixed costs
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-monthly-fixed-costs"
                                name="v020-monthly-fixed-costs"
                                type="number"
                                min="0"
                                step="0.01"
                                placeholder="1350.00"
                                aria-describedby="monthly-fixed-costs-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="v020-monthly-fixed-costs-hint"
                            class="applicant-request__hint"
                        >
                            Recurring living costs excluding debt payments.
                        </small>
                    </div>

                    <!-- Existing monthly debt payments -->
                    <div class="applicant-request__field">
                        <label for="v020-existing-debt-payments">
                            Existing debt payments
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-existing-debt-payments"
                                name="v020-existing-monthly-debt-payments"
                                type="number"
                                min="0"
                                step="0.01"
                                placeholder="180.00"
                                aria-describedby="existing-debt-payments-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="v020-existing-debt-payments-hint"
                            class="applicant-request__hint"
                        >
                            Total monthly payments for existing credit obligations.
                        </small>
                    </div>

                    <!-- Cash reserve -->
                    <div class="applicant-request__field">
                        <label for="cash-reserve">
                            Cash reserve
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-cash-reserve"
                                name="v020-cash-reserve"
                                type="number"
                                min="0"
                                step="0.01"
                                placeholder="18000.00"
                                aria-describedby="cash-reserve-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="v020-cash-reserve-hint"
                            class="applicant-request__hint"
                        >
                            Immediately available liquid savings.
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
                        <label for="v020-loan-amount">
                            Loan amount
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-loan-amount"
                                name="v020-loan-amount"
                                type="number"
                                min="500"
                                max="1000000"
                                step="1"
                                placeholder="12000.00"
                                aria-describedby="loan-amount-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                EUR
                            </span>
                        </div>

                        <small
                            id="v020-loan-amount-hint"
                            class="applicant-request__hint"
                        >
                            Principal amount requested by the applicant.
                        </small>
                    </div>

                    <!-- Annual interest rate -->
                    <div class="applicant-request__field">
                        <label for="v020-annual-interest-rate">
                            Annual interest rate
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-annual-interest-rate"
                                name="v020-annual-interest-rate"
                                type="number"
                                min="0"
                                max=""
                                step="0.01"
                                placeholder="5.20"
                                aria-describedby="annual-interest-rate-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                %
                            </span>
                        </div>

                        <small
                            id="v020-annual-interest-rate-hint"
                            class="applicant-request__hint"
                        >
                            Nominal annual interest rate in percent.
                        </small>
                    </div>

                    <!-- Loan term -->
                    <div class="applicant-request__field">
                        <label for="v020-loan-term-months">
                            Loan term
                        </label>

                        <div class="applicant-request__input-wrapper">
                            <input
                                id="v020-loan-term-months"
                                name="v020-loan-term-months"
                                type="number"
                                min="1"
                                max="120"
                                step="1"
                                placeholder="36"
                                aria-describedby="loan-term-months-hint"
                                required
                            >

                            <span class="applicant-request__input-unit">
                                months
                            </span>
                        </div>

                        <small
                            id="v020-loan-term-months-hint"
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