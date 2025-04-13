import numpy as np
from backend.mcda.core.core import Criterion, Alternative, DecisionMatrix


class Promethee:
    def __init__(self, decision_matrix: DecisionMatrix, weights: list, preference_type: list, p_values: list = [], q_values: list = []):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.preference_type = preference_type
        self.q_values = q_values
        self.p_values = p_values
        self.net_flows = None
        self.decision_matrix.beneficiate_matrix()

    def preference_function(self, d, crit_index):
        pref_type = self.preference_type[crit_index]
        p = float(self.p_values[crit_index])
        q = float(self.q_values[crit_index])

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
        else:
            return 0 if d <= 0 else 1

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
                    d = self.decision_matrix.beneficial_matrix[i][k] - self.decision_matrix.beneficial_matrix[j][k]
                    pref = self.preference_function(d, k)
                    weighted_pref = self.weights[k] * pref
                    preference_sum += weighted_pref
                preference_matrix[i][j] = preference_sum

        positive_flows = np.sum(preference_matrix, axis=1)
        negative_flows = np.sum(preference_matrix, axis=0)
        self.net_flows = positive_flows - negative_flows

    def calculate_promethee(self):
        self.calculate_flows()

        result = []
        for i in range(self.decision_matrix.alt_count):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": self.net_flows[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)
        return result
