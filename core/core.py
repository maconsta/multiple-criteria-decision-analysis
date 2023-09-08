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
    
    def __init__(self, name: str, min_max: str,sub_criteria = None):
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
    def __init__(self, criteria: list, alternatives: list):
        '''self.criteria = criteria #this is the old one
        self.alternatives = alternatives
        self.crit_count = len(criteria)
        self.alt_count = len(alternatives)
        self.normalized_matrix = np.zeros((self.alt_count, self.crit_count))
        self.matrix = np.zeros((self.alt_count, self.crit_count))

        for alt_index in range(self.alt_count):
            self.matrix[alt_index] = alternatives[alt_index].values
        '''
        self.criteria = criteria #this is new one made for both topsis and ahp.
        self.alternatives = alternatives
        self.crit_count = sum([1 + len(crit.sub_criteria) for crit in self.criteria])
        self.alt_count = len(alternatives)
        self.normalized_matrix = np.zeros((self.alt_count, self.crit_count))
        self.matrix = np.zeros((self.alt_count, self.crit_count))

        for alt_index in range(self.alt_count):
            self.matrix[alt_index] = alternatives[alt_index].values

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
        column_sums = np.sum(np.abs(self.matrix), axis=0) #calculate the sum of absolute values in each column
        self.normalized_matrix = self.matrix / column_sums #divide each element in the matrix by the corresponding column sum 

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
        norm = np.linalg.norm(self.matrix, axis=0)
        self.normalized_matrix = self.matrix / norm

        for j in range(self.crit_count):
            if self.criteria[j].min_max == 'min':
                self.normalized_matrix[:, j] *= -1
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
    
    def Eigen_normalized(self):
        '''
        Returns the normalized Eigenvector as the weight vector.
        
        Returns:
        --------
            ndarray: Normalized Eigenvector
        '''
        
        #Calculate the Eigenvalue and Eigenvector
        eigenvalues, eigenvectors = np.linalg.eig(self.P)
        
        #Take the real part of the Eigenvectors
        real_eigenvectors = np.real(eigenvectors)
        
        #Use the first column of the Eigenvectors for the Eigenvector normalization
        first_eigenvector = real_eigenvectors[:, 0]
        
        #Normalize so that the sum becomes 1
        normalized_eigenvector = first_eigenvector / np.sum(first_eigenvector)
        
        return normalized_eigenvector
# ---------------------------------------------CLASS_PAIRWISE_END-------------------------------------------------------
