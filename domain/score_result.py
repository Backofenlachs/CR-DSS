#Score_result.py

from dataclasses import dataclass



@dataclass
class ScoreResult:
    total_score: int
    risk_category: str
    breakdown: dict

    