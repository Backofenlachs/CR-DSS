class ScoringModel:

    def __init__(self):
        print("create ScoringModel")
        pass

    def evaluate(self, total_dti, residual_income_after_loan) -> str:
        
        ## results
        
        if (total_dti <= 0.35 and residual_income_after_loan >= 500):
            return "APPROVED"
        elif (total_dti <= 0.45 and residual_income_after_loan >= 250):
            return "REVIEW"
        else:
            return "DECLINED"
