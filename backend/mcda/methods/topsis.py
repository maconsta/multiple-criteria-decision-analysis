import numpy as np
import backend.mcda.core.core as core


class Topsis:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights):
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
        self.decision_matrix.normalized_matrix *= self.weights

    def calculate_topsis(self):
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

# test, delete later
# c1 = core.Criterion("style", "max")
# c2 = core.Criterion("reliability", "max")
# c3 = core.Criterion("economy", "max")
# c4 = core.Criterion("price", "min")
# criteria2 = [c1, c2, c3, c4]
#
# a1 = core.Alternative("Honda", [7, 9, 9, 8])
# a2 = core.Alternative("Saturn", [8, 7, 8, 7])
# a3 = core.Alternative("Ford", [9, 6, 8, 9])
# a4 = core.Alternative("Mazda", [6, 7, 8, 6])
# alternatives2 = [a1, a2, a3, a4]
#
# dm = core.DecisionMatrix(criteria2, alternatives2, core.DecisionMatrix.normalize_l2)
# topsis = Topsis(decision_matrix=dm, weights=[0.1, 0.4, 0.4, 0.2])
# print(topsis.calculate_topsis())
