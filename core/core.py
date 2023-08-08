import numpy as np


# ---------------------------------------------CLASS_CRITERION_START----------------------------------------------------
class Criterion:

    def __init__(self, name, crit_type, min_max):
        self.name = name
        self.crit_type = crit_type
        self.min_max = min_max
# ---------------------------------------------CLASS_CRITERION_END------------------------------------------------------

# ---------------------------------------------CLASS_ALTERNATIVE_START------------------------------------------------------
class Alternative:
    def __init__(self, name: str, criteria: list, values: list):
        self.name = name
        self.criteria = criteria
        self.values = values
# ---------------------------------------------CLASS_ALTERNATIVE_END------------------------------------------------------

# ---------------------------------------------CLASS_DECISION_MATRIX_START----------------------------------------------
class DecisionMatrix:
    def __init__(self, criteria: list, alternatives: list):
        self.criteria = criteria
        self.alternatives = alternatives
        self.crit_count = len(criteria)
        self.alt_count = len(alternatives)
        self.normalized_matrix = np.zeros((self.alt_count, self.crit_count))
        self.matrix = np.zeros((self.alt_count, self.crit_count))

        for alt_index in range(self.alt_count):
            self.matrix[alt_index] = alternatives[alt_index].values

    def normalize(self):
        max_values = np.max(self.matrix, axis=0)
        min_values = np.min(self.matrix, axis=0)
        
        for i in range(self.alt_count):
            for j in range(self.crit_count):
                if (self.criteria[j].min_max == "max"):
                    self.normalized_matrix[i][j] = self.matrix[i][j]/max_values[j]
                elif (self.criteria[j].min_max == "min"):
                    self.normalized_matrix[i][j] = min_values[j]/self.matrix[i][j] # is this valid?


    # updated version of normalize method where the chance of error when we need min method is minimal or none.
    # Please check this method again and test it too!!!
    def normalize_updated(self):
        max_values = np.max(self.matrix, axis=0)
        min_values = np.min(self.matrix, axis=0)

        for i in range(self.alt_count):
            for j in range(self.crit_count):
                if (self.criteria[j].min_max == "max"):
                    self.normalized_matrix[i][j] = self.matrix[i][j] / max_values[j]
                elif (self.criteria[j].min_max == "min"):
                    if max_values[j] - min_values[j] != 0: # ensures that zero range does not lead to a division by zero error.
                        self.normalized_matrix[i][j] = 1 - ((self.matrix[i][j] - min_values[j]) / (max_values[j] - min_values[j]))
                    else: 
                        self.normalized_matrix[i][j] = 1 # not sure if this is good idea to force the value to 1, but you will write your comment here.


    def normalize_l2(self):
        norm = np.linalg.norm(self.matrix, axis=0)
        self.normalized_matrix = self.matrix / norm

        for j in range(self.crit_count):
            if self.criteria[j].min_max == 'min':
                self.normalized_matrix[:, j] *= -1
        
        self.normalized_matrix = self.normalized_matrix
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
