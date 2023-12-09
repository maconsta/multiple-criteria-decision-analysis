import numpy as np
import core.core as core


class WeightedSum:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights

    def calculate_weighted_sum(self):
        self.decision_matrix.normalize()
        normalized_matrix = self.decision_matrix.normalized_matrix
        weighted_sum = np.matmul(normalized_matrix, np.array(self.weights))

        result = []
        for i in range(len(weighted_sum)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": weighted_sum[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)

        return result
