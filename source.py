import numpy as np


#---------------------------------------------CLASS_CRITERION_START----------------------------------------------------
class Criterion:
    def __init__(self, name, critType, minMax):
        self.name = name
        self.critType = critType
        self.minMax = minMax
#---------------------------------------------CLASS_CRITERION_END------------------------------------------------------


#---------------------------------------------CLASS_DECISION_PROBLEM_START---------------------------------------------
class DecisionProblem:
    def __init__(self, clist, alist, decisionM):
        self.criteria = clist
        self.alternatives = alist
        self.decisionMatrix = decisionM
#---------------------------------------------CLASS_DECISION_PROBLEM_END-----------------------------------------------


#---------------------------------------------CLASS_DECISION_MATRIX_START----------------------------------------------
class DecisionMatrix:
    def __init__(self, crit, alt):
        self.criteria = crit
        self.alternates = alt
        self.M = np.zeros((alt, crit))
        self.normalized_matrix = None
        self.ideal_positive_solution = None
        self.ideal_negative_solution = None

    def setAlt(self, altnum, altlist):
        if altnum <= self.alternates and len(altlist) == self.criteria:
            self.M[altnum] = altlist

    def setCrit(self, critnum, critlist):
        if critnum <= self.criteria and len(critlist) == self.alternates:
            for i in range(self.alternates):
                self.M[i][critnum] = critlist[i]

    def normalize(self):
        max_values = np.max(self.M, axis=0)
        self.normalized_matrix = self.M / max_values

    def calculate_ideal_solutions(self, weights):
        positive_ideal = np.amax(self.normalized_matrix, axis=0)
        negative_ideal = np.amin(self.normalized_matrix, axis=0)
        self.ideal_positive_solution = positive_ideal * weights
        self.ideal_negative_solution = negative_ideal * weights

    def calculate_distances(self):
        positive_distances = np.linalg.norm(self.normalized_matrix - self.ideal_positive_solution, axis=1)
        negative_distances = np.linalg.norm(self.normalized_matrix - self.ideal_negative_solution, axis=1)
        return positive_distances, negative_distances

    def calculate_closeness(self, positive_distances, negative_distances):
        total_distances = positive_distances + negative_distances
        closeness = negative_distances / total_distances
        return closeness
#---------------------------------------------CLASS_DECISION_MATRIX_END-----------------------------------------------


#----------------------------------------------TOPSIS_START-----------------------------------------------------------  
    #TOPSIS Method
    def topsis(self, weights):
        self.normalize()
        self.calculate_ideal_solutions(weights)
        positive_distances, negative_distances = self.calculate_distances()
        closeness = self.calculate_closeness(positive_distances, negative_distances)
        best_alternative_index = np.argmax(closeness)
        best_alternative_closeness = closeness[best_alternative_index]
        return closeness, best_alternative_index, best_alternative_closeness
#----------------------------------------------TOPSIS_END--------------------------------------------------------------


#---------------------------------------------TOPSIS_PAIRWISE_START----------------------------------------------------    
    #TOPSIS Method using Pairwise
    def topsis_PW(self, weights):
        self.normalize()

        pw = Pairwise(self.criteria)
        for i in range(self.criteria):
            for j in range(i + 1, self.criteria):
                pw.setComparson(i, j, self.M[:, i].dot(self.M[:, j]))

        weights = np.array(weights)
        eigen_values = pw.Eigen()
        normalized_eigen_values = eigen_values / np.sum(eigen_values)

        weighted_matrix = self.M * weights
        positive_ideal_solution = np.max(weighted_matrix, axis=0)
        negative_ideal_solution = np.min(weighted_matrix, axis=0)

        positive_distances = np.linalg.norm(weighted_matrix - positive_ideal_solution, axis=1)
        negative_distances = np.linalg.norm(weighted_matrix - negative_ideal_solution, axis=1)

        closeness = negative_distances / (positive_distances + negative_distances)
        best_alternative_index = np.argmax(closeness)

        return closeness, best_alternative_index
#---------------------------------------------TOPSIS_PAIRWISE_END------------------------------------------------------


#---------------------------------------------CLASS_PAIRWISE_START-----------------------------------------------------
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
#---------------------------------------------CLASS_PAIRWISE_END-------------------------------------------------------
    

#---------------------------------------------PRINT_MATRIX_START-------------------------------------------------------
def printMatrix(m):
    for row in m:
        s = ' '.join([str(x) for x in row])
        print(s)
#---------------------------------------------PRINT_MATRIX_END---------------------------------------------------------


#---------------------------------------------DEFAULT_EXAMPLE_START----------------------------------------------------
'''''
dm = DecisionMatrix(alt=3, crit=4)
dm.setAlt(0, [0.751, 0.480, 0.077, 0.066])
dm.setAlt(1, [0.178, 0.406, 0.231, 0.615])
dm.setAlt(2, [0.071, 0.114, 0.692, 0.319])
print(dm.M)

dm.setCrit(0, [1,2,3,4])
print(dm.M)

# Test with weights put directly, precalculated
weights = [0.232, 0.402, 0.061, 0.305]
final = dm.weigh(weights)
print('=======================FINAL=================')
print(final)
print('=======================FINAL=================')


#Calculating the weights by pairwise comparison
pw = Pairwise(4)
printMatrix(pw.P)
pw.setComparson(0, 1, 1/3)
pw.setComparson(0, 2, 5)
pw.setComparson(0, 3, 1)
pw.setComparson(1, 2, 5)
pw.setComparson(1, 3, 1)
pw.setComparson(2, 3, 1/5)
print('=======================PAIRWISE MATRIX=================')
printMatrix(pw.P)
print('=======================PAIRWISE MATRIX=================')

eigen = pw.Eigen()
print(eigen)
'''
#---------------------------------------------DEFAULT_EXAMPLE_END------------------------------------------------------


#---------------------------------------------TOPSIS_EXAMPLE_START-----------------------------------------------------
'''''
# TOPSIS Example
dm = DecisionMatrix(alt=3, crit=4)
dm.setAlt(0, [0.751, 0.480, 0.077, 0.066])
dm.setAlt(1, [0.178, 0.406, 0.231, 0.615])
dm.setAlt(2, [0.071, 0.114, 0.692, 0.319])

weights = [0.232, 0.402, 0.061, 0.305]
closeness, best_alternative_index, best_alternative_closeness = dm.topsis(weights)

print("Closeness:")
print(closeness)

print("Best Alternative Index:", best_alternative_index + 1)
#print("Best Alternative Closeness:", best_alternative_closeness)

'''
#---------------------------------------------TOPSIS_EXAMPLE_END-------------------------------------------------------


#---------------------------------------------TOPSIS_PAIRWISE_EXAMPLE_START--------------------------------------------
# TOPSIS Using Pairwise Example
dm = DecisionMatrix(alt=3, crit=4)
dm.setAlt(0, [0.751, 0.480, 0.077, 0.066])
dm.setAlt(1, [0.178, 0.406, 0.231, 0.615])
dm.setAlt(2, [0.071, 0.114, 0.692, 0.319])

weights = [0.232, 0.402, 0.061, 0.305]
closeness, best_alternative_index = dm.topsis_PW(weights)

print("Closeness:")
print(closeness)

print("Best Alternative Index:", best_alternative_index + 1)
#---------------------------------------------TOPSIS_PAIRWISE_EXAMPLE_END----------------------------------------------


