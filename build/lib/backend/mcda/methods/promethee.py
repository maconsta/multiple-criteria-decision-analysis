import numpy as np
from mcda.core.core import Criterion, Alternative, DecisionMatrix


class Promethee:
    def __init__(self, decision_matrix: DecisionMatrix, weights):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.performance_index_matrix = np.zeros(
            (self.decision_matrix.alt_count, self.decision_matrix.alt_count))

    def calculate_promethee(self):

        # normalise using a weird method
        # is this normalization method OK, or should another one be used?
        max_values = np.max(self.decision_matrix.matrix, axis=0)
        min_values = np.min(self.decision_matrix.matrix, axis=0)
        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.crit_count):
                self.decision_matrix.normalized_matrix[i][j] = (
                    self.decision_matrix.matrix[i][j]-min_values[j]) / (max_values[j]-min_values[j])
        # print(self.decision_matrix.normalized_matrix)

        net_flows = np.zeros(self.decision_matrix.alt_count)
        positive_flows = np.zeros(self.decision_matrix.alt_count)
        negative_flows = np.zeros(self.decision_matrix.alt_count)

        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if i != j:
                    for k in range(self.decision_matrix.crit_count):
                        diff = self.decision_matrix.normalized_matrix[i][k] - \
                            self.decision_matrix.normalized_matrix[j][k]
                        if diff > 0:
                            positive_flows[i] += self.weights[k] * diff
                        else:
                            negative_flows[i] += self.weights[k] * (-diff)

            net_flows[i] = positive_flows[i] - negative_flows[i]

        # print(positive_flows)
        # print(negative_flows)
        # print(net_flows)

        result = []
        for i in range(len(net_flows)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": net_flows[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)

        return result


# c1 = Criterion("c1", "max")
# c2 = Criterion("c2", "max")
# c3 = Criterion("c3", "max")
# c4 = Criterion("c4", "max")
# c5 = Criterion("c5", "max")
# c6 = Criterion("c6", "max")
# criteria = [c1, c2, c3, c4, c5, c6]

# a1 = Alternative("a1", [1350, 1850, 7.5, 2.58, 93.5, 0.045])
# a2 = Alternative("a2", [1680, 1650, 8.5, 3.75, 95.3, 0.068])
# a3 = Alternative("a3", [1560, 1950, 6.5, 4.86, 88.6, 0.095])
# a4 = Alternative("a4", [1470, 1850, 9.5, 3.16, 98.4, 0.072])
# alternatives = [a1, a2, a3, a4]

# dm = DecisionMatrix(criteria, alternatives)
# weights = [0.2336, 0.1652, 0.3355, 0.1021, 0.0424, 0.1212]

# promethee = Promethee(dm, weights)
# print(promethee.calculate_promethee())
