"""
xgboost_model.py

XGBoost classifier.
Strong classical benchmark.
"""

from xgboost import XGBClassifier


class XGBoostModel:

    def build(self):

        return XGBClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
            eval_metric="logloss"
        )