import numpy as np
import core.core as core


class WeightedSum:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.best_alternative = None
        self.best_alternative_index = None

    def calculate_weighted_sum(self):
        self.decision_matrix.normalize()
        normalized_matrix = self.decision_matrix.normalized_matrix
        weighted_sum = np.matmul(normalized_matrix, np.array(self.weights))
        self.best_alternative_index = np.argmax(weighted_sum)
        self.best_alternative = weighted_sum[self.best_alternative_index]
        return weighted_sum#, self.best_alternative, self.best_alternative_index



