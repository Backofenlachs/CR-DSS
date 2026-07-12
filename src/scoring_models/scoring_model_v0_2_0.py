class ScoringModel2: 

    REQUIRED_DATA = [
        "employment_months",
        "age",
        "total_dti",
        "residual_income_after_loan",
        "reserve_coverage_months",
    ]

    def dtiRisk(self, dti):
        if dti <= 0.30:   return 0
        elif dti <= 0.40: return 10
        elif dti <= 0.50: return 25
        elif dti > 0.50:  return 50
        else:   
            raise ValueError(
                f"[ScoringModel2.dtiRisk] total_dti invalid: {dti}"
            )

    def residualIncomeRisk(self, rial):
        if rial >= 800:     return 0
        elif rial >= 500:   return 10
        elif rial >= 250:   return 25
        elif rial < 250:    return 50
        else:
            raise ValueError(
                f"[ScoringModel2.residualIncomeRisk] residual_income_after_loan invalid: {rial}"
            )

    def reserveCoverageRisk(self, rcm):
        if rcm >= 6:    return 0
        elif rcm >= 3:  return 10
        elif rcm >= 1:  return 25
        elif rcm <= 1:  return 50
        else:
            raise ValueError(
                f"[ScoringModel2.reserveCoverageRisk] reserve_coverage_months invalid: {rcm}"
            )
        

    def employmentStabilityRisk(self, esr):
        if esr >= 24:   return 0
        elif esr >= 12: return 10
        elif esr >= 6:  return 25
        elif esr < 6:   return 50
        else:
            raise ValueError(
                f"[ScoringModel2.employmentStabilityRisk] employment_months invalid: {esr}"
            )

    def ageRisk(self, age):
        if   25 <= age <= 60:   return 0
        elif 18 <= age <= 24:   return 10
        elif 61 <= age <= 70:   return 15
        elif 70  < age:         return 30
        else:   
            raise ValueError(
                f"alter muss mindestens 18 sein"
            )

    def evaluate(self, data):
        dtiScore = self.dtiRisk(data['total_dti'])
        residualScore = self.residualIncomeRisk(data['residual_income_after_loan'])
        reserveScore = self.reserveCoverageRisk(data['reserve_coverage_months'])
        employScore = self.employmentStabilityRisk(data['employment_months'])
        ageScore = self.ageRisk(data['age'])

        riskScore = dtiScore + residualScore + reserveScore + employScore + ageScore

        # Decision Logic

        if riskScore <= 50 and data['total_dti'] <= 0.40 and data['residual_income_after_loan']:
            return "APPROVED"
        elif riskScore <= 120 and data['residual_income_after_loan'] >= 250:
            return "REWIEV"
        else:
            return "DECLINED"
