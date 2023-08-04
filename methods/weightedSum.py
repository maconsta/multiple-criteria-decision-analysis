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
        weighted_sum = np.dot(normalized_matrix, self.weights)
        self.best_alternative_index = np.argmax(weighted_sum)
        self.best_alternative = weighted_sum[self.best_alternative_index]
        return weighted_sum, self.best_alternative, self.best_alternative_index


# Run the file from the console: python -m methods.weightedSum
# or there will be an error

dm = core.DecisionMatrix(crit_count=4, alt_count=3)
dm.set_alternative(0, [0.751, 0.480, 0.077, 0.066])
dm.set_alternative(1, [0.178, 0.406, 0.231, 0.615])
dm.set_alternative(2, [0.071, 0.114, 0.692, 0.319])

weights = [0.232, 0.402, 0.061, 0.305]

weighted_sum = WeightedSum(dm, weights)
result, best_alternative, best_alternative_index = weighted_sum.calculate_weighted_sum()

print(result)
print("Best Alternative Index: ", best_alternative_index + 1)