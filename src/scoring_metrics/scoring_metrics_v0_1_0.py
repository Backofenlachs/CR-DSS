class ScoringModel1:

    REQUIRED_DATA = [
        "total_dti",
        "residual_income_after_loan"
    ]

    def __init__(self):
        print("create ScoringModel")
        pass

    def evaluate(self, data) -> str:
        
        total_dti = data['total_dti']
        residual_income_after_loan = data['residual_income_after_loan']
        ## results
        
        if (total_dti <= 0.35 and residual_income_after_loan >= 500):
            return "APPROVED"
        elif (total_dti <= 0.45 and residual_income_after_loan >= 250):
            return "REVIEW"
        else:
            return "DECLINED"
