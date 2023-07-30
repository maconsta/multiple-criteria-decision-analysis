import numpy as np
import core.core as core


class Topsis:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.ideal_positive_solution = []
        self.ideal_negative_solution = []

    def calculate_ideal_solutions(self):
        positive_ideal = np.amax(
            self.decision_matrix.normalized_matrix, axis=0)
        negative_ideal = np.amin(
            self.decision_matrix.normalized_matrix, axis=0)
        self.ideal_positive_solution = positive_ideal * self.weights
        self.ideal_negative_solution = negative_ideal * self.weights

    def calculate_distances(self):
        positive_distances = np.linalg.norm(
            self.decision_matrix.normalized_matrix - self.ideal_positive_solution, axis=1)
        negative_distances = np.linalg.norm(
            self.decision_matrix.normalized_matrix - self.ideal_negative_solution, axis=1)
        return positive_distances, negative_distances

    def calculate_closeness(self, positive_distances, negative_distances):
        total_distances = positive_distances + negative_distances
        closeness = negative_distances / total_distances
        return closeness

    def calculate_topsis(self):
        self.decision_matrix.normalize()
        self.calculate_ideal_solutions()
        positive_distances, negative_distances = self.calculate_distances()
        closeness = self.calculate_closeness(positive_distances, negative_distances)
        best_alternative_index = np.argmax(closeness)
        best_alternative_closeness = closeness[best_alternative_index]
        return closeness, best_alternative_index, best_alternative_closeness

 
# Run the file from the console: python -m methods.topsis
# or there will be an error

# dm = core.DecisionMatrix(crit_count=4, alt_count=3)
# dm.set_alternative(0, [0.751, 0.480, 0.077, 0.066])
# dm.set_alternative(1, [0.178, 0.406, 0.231, 0.615])
# dm.set_alternative(2, [0.071, 0.114, 0.692, 0.319])

# weights = [0.232, 0.402, 0.061, 0.305]

# topsis = Topsis(dm, weights)

# closeness, best_alternative_index, best_alternative_closeness = topsis.calculate_topsis()

# print("Closeness:")
# print(closeness)

# print("Best Alternative Index:", best_alternative_index + 1)

