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
        
        self.criteria = criteria #this is the old one
        self.alternatives = alternatives
        self.crit_count = len(criteria)
        self.alt_count = len(alternatives)
        self.normalized_matrix = np.zeros((self.alt_count, self.crit_count))
        self.matrix = np.zeros((self.alt_count, self.crit_count))

        for alt_index in range(self.alt_count):
            self.matrix[alt_index] = alternatives[alt_index].values
        
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
        
        if self.crit_count != self.matrix.shape[1]:
            raise ValueError("Dimension mismatch: number of criteria must match the number of columns in the decision matrix")
        
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
    Class Pairwise, contains the pairwise matrix and a procedure to return the eigenvector

    Attributes
    ==========

    criteria : list 
        a list of Criterion objects

    pairwise_matrix: numpy 2d array (list of lists)
        the pairwise matrix
    """
    
    def __init__(self, criteria: list):
        self.criteria = criteria
        self.crit_count = len(criteria)
        self.pairwise_matrix = np.zeros((self.crit_count, self.crit_count))
    
    def fill_matrix(self):
        # would be a good idea to move the input to another class, responsible only for the input of data 
        for row in range(self.crit_count):
            for col in range(self.crit_count):
                if row == col:
                    self.pairwise_matrix[row][col] = 1
                    continue

                if self.pairwise_matrix[row][col] == 0:
                    print("How important is", self.criteria[row].name, "with respect to", self.criteria[col].name)
                    user_input = float(input("Enter: "))
                    self.pairwise_matrix[row][col] = user_input
                    self.pairwise_matrix[col][row] = 1 / user_input

    def calculate_eigenvector(self):
        eigenvector = np.zeros(self.crit_count)
        temp_matrix = self.pairwise_matrix
        while(True):
            temp_matrix = np.matmul(temp_matrix, temp_matrix)
            row_sums = np.sum(temp_matrix, axis=1)
            row_sum_totals = np.sum(row_sums)
            new_eigenvector = row_sums / row_sum_totals
            if np.all(np.isclose(eigenvector, new_eigenvector)):
                return eigenvector
            
            eigenvector = new_eigenvector

        
                

# c1 = Criterion("c1", "max")
# c2 = Criterion("c2", "max")
# c3 = Criterion("c3", "max")
# criteria = [c1, c2, c3]

# pw = Pairwise(criteria)
# pw.fill_matrix()
# weights = pw.calculate_eigenvector()

# ---------------------------------------------CLASS_PAIRWISE_END-----------------------------------------------------