import numpy as np
import core.core as core


class Topsis:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix  # DOES IT MAKE A COPY HERE?
        self.weights = weights
        self.ideal_positive_solution = []
        self.ideal_negative_solution = []

    def calculate_ideal_solutions(self):
        self.ideal_positive_solution = np.amax(
            self.decision_matrix.normalized_matrix, axis=0)
        self.ideal_negative_solution = np.amin(
            self.decision_matrix.normalized_matrix, axis=0)

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

    def weigh(self):
        for col in range(self.decision_matrix.normalized_matrix.shape[0]):
            self.decision_matrix.normalized_matrix[:, col] *= self.weights[col]

    def calculate_topsis(self):
        self.decision_matrix.normalize_l2()
        self.weigh()
        self.calculate_ideal_solutions()
        positive_distances, negative_distances = self.calculate_distances()
        closeness = self.calculate_closeness(
            positive_distances, negative_distances)

        result = []
        for i in range(len(closeness)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": closeness[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)

        return result
