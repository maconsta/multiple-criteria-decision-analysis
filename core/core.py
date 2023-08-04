import numpy as np


# ---------------------------------------------CLASS_CRITERION_START----------------------------------------------------
class Criterion:

    def __init__(self, name, crit_type, min_max):
        self.name = name
        self.crit_type = crit_type
        self.min_max = min_max
# ---------------------------------------------CLASS_CRITERION_END------------------------------------------------------


# ---------------------------------------------CLASS_DECISION_MATRIX_START----------------------------------------------
class DecisionMatrix:
    def __init__(self, crit_count, alt_count):
        self.crit_count = crit_count
        self.alt_count = alt_count
        self.matrix = np.zeros((alt_count, crit_count))
        self.normalized_matrix = np.zeros((alt_count, crit_count))

    def set_alternative(self, row_index, alt_list):
        if row_index <= self.alt_count and len(alt_list) == self.crit_count:
            self.matrix[row_index] = alt_list

    def set_criteria(self, col_index, crit_list):
        if col_index <= self.crit_count and len(crit_list) == self.alt_count:
            for i in range(self.alt_count):
                self.matrix[i][col_index] = crit_list[i]

    def normalize(self):
        max_values = np.max(self.matrix, axis=0)
        self.normalized_matrix = self.matrix / max_values

    def normalize_l2(self):
        norm = np.linalg.norm(self.matrix, axis=0)
        self.normalized_matrix = self.matrix / norm
# ---------------------------------------------CLASS_DECISION_MATRIX_END-----------------------------------------------


# ---------------------------------------------CLASS_PAIRWISE_START-----------------------------------------------------
class Pairwise:
    def __init__(self, crit):
        self.criteria = crit
        self.P = np.ones((crit, crit))
        np.fill_diagonal(self.P, 1)

    def setComparson(self, crit1, crit2, val):
        if crit1 <= self.criteria and crit2 <= self.criteria:
            self.P[crit1][crit2] = val
            self.P[crit2][crit1] = 1 / val

    def Eigen(self):
        result = np.ones(self.criteria)
        total = 0
        for j in range(self.criteria):
            for i in range(self.criteria):
                result[j] *= self.P[j][i]
            result[j] = np.power(result[j], 1 / self.criteria)
            total += result[j]
        result /= total
        return result
# ---------------------------------------------CLASS_PAIRWISE_END-------------------------------------------------------
