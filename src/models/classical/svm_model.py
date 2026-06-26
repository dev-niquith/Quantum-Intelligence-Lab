"""
svm_model.py

Support Vector Machine.
"""

from sklearn.svm import SVC


class SVMModel:

    def build(self):

        return SVC(

            kernel="rbf",

            #probability=True,

            random_state=42
        )