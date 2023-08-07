
import numpy as np
from core.core import DecisionMatrix, Pairwise
from methods.topsis import Topsis


class TopsisPairwise():
    def __init__(self, decision_matrix: DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.pairwise = Pairwise(decision_matrix.crit_count)

    def calculate_pairwise_comparisons(self):
        for i in range(self.decision_matrix.crit_count - 1):
            for j in range(i+1, self.decision_matrix.crit_count):
                val = self.weights[i] / self.weights[j]
                self.pairwise.setComparson(i, j, val)
                self.pairwise.setComparson(j, i, 1/val)

    def calculate_topsis(self):
        self.decision_matrix.normalize()
        self.calculate_pairwise_comparisons()
        eigenvalues = self.pairwise.Eigen()
        weighted_eigenvalues = eigenvalues * self.weights
        # Set the first criterion of decision matrix with weighted eigenvalues
        self.decision_matrix.set_criteria(0, weighted_eigenvalues)
        closeness, best_alternative_index, best_alternative_closeness = super().calculate_topsis() # to fix; this calculates normal topsis
        return closeness, best_alternative_index, best_alternative_closeness

# Run the file from the console: python -m methods.topsisPairwise
# or there will be an error

weights = [0.232, 0.402, 0.061, 0.305]

dm = DecisionMatrix(crit_count=4, alt_count=3)
dm.set_alternative(0, [0.751, 0.480, 0.077, 0.066])
dm.set_alternative(1, [0.178, 0.406, 0.231, 0.615])
dm.set_alternative(2, [0.071, 0.114, 0.692, 0.319])

pw = TopsisPairwise(dm, weights)

closeness, best_alternative_index, best_alternative_closeness = pw.calculate_topsis()

print("Closeness:")
print(closeness)

print("Best Alternative Index:", best_alternative_index + 1)
