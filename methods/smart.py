import numpy as np
import core.core as core

class SMART:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights

    def weigh(self):
        for col in range(self.decision_matrix.normalized_matrix.shape[1]):
            self.decision_matrix.normalized_matrix[:, col] *= self.weights[col]
    
    # this is another function to normalize in this method.
    # def normalize(self):
    #     column_sums = np.sum(self.decision_matrix.matrix, axis=0)
    #     self.decision_matrix.normalized_matrix = self.decision_matrix.matrix / column_sums

    def calculate_smart(self):
        self.decision_matrix.normalize_l2()  # Using L2 normalization from core
        self.weigh()

        scores = np.sum(self.decision_matrix.normalized_matrix, axis=1)
        result = []

        for i in range(len(scores)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": scores[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)

        return result

        