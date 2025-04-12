import math
import numpy as np


# ---------------------------------------------CLASS_CRITERION_START----------------------------------------------------
class Criterion:
    """
    Class Criterion, represents a single criterion

    Attributes
    ==========

    name : str
        name of the criterion

    min_max : str 
        minimize or maximise the criterion; accepted values are "min" or "max"
        
    sub_criteria
        adding sub criteria for AHP method
    """

    def __init__(self, name: str, min_max: str, sub_criteria=None):
        self.name = name
        self.min_max = min_max
        self.sub_criteria = sub_criteria if sub_criteria else []


# ---------------------------------------------CLASS_CRITERION_END------------------------------------------------------

# ---------------------------------------------CLASS_ALTERNATIVE_START------------------------------------------------------


class Alternative:
    """
    Class Alternative, represents a single alternative

    Attributes
    ==========

    name : str
        name of the alternative

    values : list 
        a list of values
    """

    def __init__(self, name: str, values: list):
        self.name = name
        self.values = values


# ---------------------------------------------CLASS_ALTERNATIVE_END------------------------------------------------------

# ---------------------------------------------CLASS_DECISION_MATRIX_START----------------------------------------------


class DecisionMatrix:
    def __init__(self, criteria: list, alternatives: list, normalization_method):

        self.criteria = criteria  # this is the old one
        self.alternatives = alternatives
        self.crit_count = len(criteria)
        self.alt_count = len(alternatives)
        self.matrix = np.array([alt.values for alt in alternatives], dtype=np.float64)
        self.normalized_matrix = np.zeros((self.alt_count, self.crit_count), dtype=np.float64)

        if normalization_method is None:
            normalization_method = self.normalize
        normalization_method(self)

        # self.criteria = criteria #this is new one made for both topsis and ahp.
        # self.alternatives = alternatives
        # self.crit_count = sum([1 + len(crit.sub_criteria) for crit in self.criteria])
        # self.alt_count = len(alternatives)
        # self.normalized_matrix = np.zeros((self.alt_count, self.crit_count))
        # self.matrix = np.zeros((self.alt_count, self.crit_count))

        # for alt_index in range(self.alt_count):
        #     self.matrix[alt_index] = alternatives[alt_index].values

    def normalize(self):
        '''
        Normalize the decision matrix using the linear norm

        Returns:
        --------
            None
        '''
        max_values = np.max(self.matrix, axis=0)
        absolute_max_values = np.max(np.absolute(self.matrix), axis=0)

        for i in range(len(absolute_max_values)):
            if absolute_max_values[i] == 0:
                # set values to 0.1 to avoid division by zero
                absolute_max_values[i] = 0.1

        for i in range(self.alt_count):
            for j in range(self.crit_count):
                if (self.criteria[j].min_max == "max"):
                    self.normalized_matrix[i][j] = self.matrix[i][j] / \
                                                   max_values[j]
                elif (self.criteria[j].min_max == "min"):
                    self.normalized_matrix[i][j] = (
                                                           self.matrix[i][j] * -1) / absolute_max_values[j]

    def normalize_l1(self):
        '''
        Normalize the decision matrix using L1 normalization

        Returns:
        --------
            None
        '''
        column_sums = np.sum(np.abs(self.matrix), axis=0)  # calculate the sum of absolute values in each column
        self.normalized_matrix = self.matrix / column_sums  # divide each element in the matrix by the corresponding column sum

        for j in range(self.crit_count):
            if self.criteria[j].min_max == 'min':
                self.normalized_matrix[:, j] *= -1

    def normalize_l2(self):
        '''
        Normalize the decision matrix using the L2 vector norm

        Returns:
        --------
            None
        '''

        if self.crit_count != self.matrix.shape[1]:
            raise ValueError(
                "Dimension mismatch: number of criteria must match the number of columns in the decision matrix")

        norm = np.linalg.norm(self.matrix, axis=0)
        self.normalized_matrix = self.matrix / norm

        for j in range(self.crit_count):
            try:
                if self.criteria[j].min_max == 'min':
                    self.normalized_matrix[:, j] *= -1
            except IndexError:
                raise IndexError(f"Criteria index {j} is out of range. Length of criteria list: {len(self.criteria)}")


# ---------------------------------------------CLASS_DECISION_MATRIX_END-----------------------------------------------


# ---------------------------------------------CLASS_PAIRWISE_START-----------------------------------------------------

class Pairwise:
    """
    Returns an eigenvector from a list of values.
    The values list is a list of the results of the pairwise comparison of all alternatives/criteria pairs.

    Attributes
    ==========

    values : list
        a list of values

    entries_count: integer
        number of alternatives/criteria, used in the comparison

    pairwise_matrix: numpy 2d array
        the pairwise matrix
    """

    def __init__(self, values: list):
        self.values = values
        self.entries_count = self.__find_n_choose_k(len(values))
        self.pairwise_matrix = self.__construct_matrix(values)

    def __find_n_choose_k(self, binomial_coefficient):
        """
            The total number of pairwise comparisons is always the binomial coefficient of 'n choose k', where
            'n' is the size of the set (alternatives or criteria) and
            k is number of the selected items (pairs of comparisons)\n

            In the current implementation, 'k' will always be 2 (it is a pairwise comparison!)\n

            Returns 'n'
        """

        k = 2
        for n in range(k, 100):
            if math.comb(n, k) == binomial_coefficient:
                return n

    def __construct_matrix(self, values):
        matrix = np.zeros((self.entries_count, self.entries_count))

        values_index = 0
        for row in range(self.entries_count):
            for col in range(self.entries_count):
                if row == col:
                    matrix[row][col] = 1
                    continue
                elif matrix[row][col] == 0:
                    matrix[row][col] = values[values_index]
                    matrix[col][row] = 1 / values[values_index]
                    values_index += 1

        return matrix

    def calculate_eigenvector(self):
        # the following check is important, but TODO implement a better eigenvector method
        # if all(val == self.values[0] for val in self.values):
        #     uniform_eigenvector = np.ones(self.entries_count) / self.entries_count
        #     return uniform_eigenvector

        eigenvector = np.zeros(self.entries_count)
        temp_matrix = self.pairwise_matrix
        while True:
            temp_matrix = np.matmul(temp_matrix, temp_matrix)
            row_sums = np.sum(temp_matrix, axis=1)
            row_sum_totals = np.sum(row_sums)
            new_eigenvector = row_sums / row_sum_totals
            if np.all(np.isclose(eigenvector, new_eigenvector)):
                return eigenvector.tolist()

            eigenvector = new_eigenvector

# TEST FROM THE AHP PRESENTATION
# vals = [9, 9, 9, 9, 2, 1/2, 8, 1/7, 8, 8]
# pw = Pairwise(vals)
# print(pw.calculate_eigenvector())
# # EXPECTED RESULT [0.3194, 0.5595, 0.1211]

# ---------------------------------------------CLASS_PAIRWISE_END-----------------------------------------------------
