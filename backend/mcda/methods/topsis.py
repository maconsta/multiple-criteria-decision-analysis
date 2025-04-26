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

# test, delete later; taken from https://www.sciencedirect.com/science/article/pii/S1877705814035280
# c1 = core.Criterion("EWSC", "max")
# c2 = core.Criterion("ISDC", "max")
# c3 = core.Criterion("MPRC", "max")
# c4 = core.Criterion("MRC", "max")
# c5 = core.Criterion("SDC", "max")
# c6 = core.Criterion("ACCA", "max")
# c7 = core.Criterion("PWNGO", "max")
# c8 = core.Criterion("AOSP", "max")
# c9 = core.Criterion("LNP", "max")
# c10 = core.Criterion("IEP", "max")
# criteria = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
#
# a1 = core.Alternative("A", [150, 160, 130, 1200, 1400, 3, 4, 3, 4, 5])
# a2 = core.Alternative("B", [140, 170, 150, 1300, 1800, 5, 5, 4, 3, 4])
# a3 = core.Alternative("C", [170, 160, 180, 1350, 1480, 4, 3, 5, 5, 5])
# a4 = core.Alternative("D", [180, 165, 160, 1500, 1600, 2, 3, 3, 1, 2])
# a5 = core.Alternative("E", [110, 150, 160, 1500, 1400, 1, 3, 5, 2, 5])
# a6 = core.Alternative("F", [120, 180, 130, 1400, 1400, 5, 3, 4, 4, 2])
# a7 = core.Alternative("G", [130, 165, 150, 1300, 1750, 3, 2, 4, 3, 5])
# a8 = core.Alternative("H", [200, 160, 130, 1550, 1800, 4, 1, 2, 4, 4])
# a9 = core.Alternative("I", [150, 110, 140, 1200, 1650, 5, 2, 2, 4, 5])
# alternatives = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
#
# dm = core.DecisionMatrix(criteria, alternatives, core.DecisionMatrix.normalize_l2)
# topsis = Topsis(decision_matrix=dm, weights=[0.1078, 0.0611, .1588, .1123, .0361, .0239, .0162, .0107, .2529, .2199])
# print(topsis.calculate_topsis())
