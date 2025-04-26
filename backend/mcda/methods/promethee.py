import numpy as np

from backend.mcda.core import core
from backend.mcda.core.core import Criterion, Alternative, DecisionMatrix


class Promethee:
    def __init__(self, decision_matrix: DecisionMatrix, weights: list, preference_type: list = [], p_values: list = [],
                 q_values: list = []):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.preference_type = preference_type
        self.q_values = q_values
        self.p_values = p_values
        self.net_flows = None
        self.decision_matrix.beneficiate_matrix()

    def preference_function(self, d, crit_index):
        pref_type = self.preference_type[crit_index] if self.preference_type else None
        p = float(self.p_values[crit_index]) if self.p_values else None
        q = float(self.q_values[crit_index]) if self.q_values else None

        if pref_type == "usual":
            return 0 if d <= 0 else 1
        elif pref_type == "u-shape":
            return 0 if abs(d) <= q else 1
        elif pref_type == "v-shape":
            return 0 if abs(d) <= 0 else min(abs(d) / p, 1)
        elif pref_type == "level":
            if abs(d) <= q:
                return 0
            elif abs(d) <= p:
                return 0.5
            else:
                return 1
        elif pref_type == "linear":
            return 0 if abs(d) <= q else min((abs(d) - q) / (p - q), 1)
        elif pref_type == "gaussian":
            return 1 - np.exp(- (d ** 2) / (2 * p ** 2))
        else:  # special case for testing
            return 0 if d <= 0 else d

    def calculate_flows(self):
        alt_count = self.decision_matrix.alt_count
        crit_count = self.decision_matrix.crit_count
        preference_matrix = np.zeros((alt_count, alt_count))

        for i in range(alt_count):
            for j in range(alt_count):
                if i == j:
                    continue
                preference_sum = 0
                for k in range(crit_count):
                    d = self.decision_matrix.normalized_matrix[i][k] - self.decision_matrix.normalized_matrix[j][k]
                    pref = self.preference_function(d, k)
                    weighted_pref = self.weights[k] * pref
                    preference_sum += weighted_pref
                preference_matrix[i][j] = preference_sum

        positive_flows = np.sum(preference_matrix, axis=1) # promethee 1
        negative_flows = np.sum(preference_matrix, axis=0) # promethee 1
        normalized_positive_flows = positive_flows / (alt_count - 1) # promethee 2
        normalized_negative_flows = negative_flows / (alt_count - 1) # promethee 2

        self.net_flows = normalized_positive_flows - normalized_negative_flows

    def calculate_promethee(self):
        self.calculate_flows()

        result = []
        for i in range(self.decision_matrix.alt_count):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": self.net_flows[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)
        return result


# # test, delete later
# c1 = core.Criterion("Processor", "max")
# c2 = core.Criterion("HDC", "max")
# c3 = core.Criterion("OS", "max")
# c4 = core.Criterion("RAM", "max")
# c5 = core.Criterion("SreenSize", "max")
# c6 = core.Criterion("Brand", "max")
# c7 = core.Criterion("Color", "max")
# criteria = [c1, c2, c3, c4, c5, c6, c7]
#
# # passing already normalized values
# a1 = core.Alternative("Model 1", [0, 0, 0, 0, 0, 1, 0])
# a2 = core.Alternative("Model 2", [0.5, 0.5, 0.33333, 0, 0.66667, 0.14286, 0])
# a3 = core.Alternative("Model 3", [0.5, 1, 1, 0.5, 0.66667, 0.71429, 0.3333])
# a4 = core.Alternative("Model 4", [1, 1, 1, 1, 1, 0, 1])
# a5 = core.Alternative("Model 5", [0.5, 0.5, 1, 0.5, 0.66667, 1, 1])
# a6 = core.Alternative("Model 6", [0, 0, 0.33333, 0, 0.66667, 0.42857, 0])
# alternatives = [a1, a2, a3, a4, a5, a6]
#
# w = [0.37657, .09395, .04529, .21594, .16932, .07647, .02247]
#
# #
# dm = core.DecisionMatrix(criteria, alternatives, core.DecisionMatrix.normalize_l2)
# promethee = Promethee(decision_matrix=dm, weights=w)
# print(promethee.calculate_promethee())
