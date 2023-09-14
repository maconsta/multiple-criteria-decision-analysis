import unittest
import numpy as np
from methods.ahp import AHP
from core.core import Criterion, Alternative, DecisionMatrix

class AHPTest(unittest.TestCase):
    def runTest(self):
        #Create sub-criteria for reliability
        sub_c1 = Criterion("Mechanical", "max")
        sub_criteria_reliability = [sub_c1]
        
        #Create main criteria with sub-criteria for reliability
        c1 = Criterion("Reliability", "max", sub_criteria_reliability)
        c2 = Criterion("Style", "max")
        c3 = Criterion("Economy", "max")

        criteria2 = [c1, c2, c3]
        
        
        a1 = Alternative("Honda", [7, 9, 9])  
        a2 = Alternative("Saturn", [8, 7, 8])  
        a3 = Alternative("Ford", [9, 6, 8])
        a4 = Alternative("Mazda", [6, 7, 8])
        alternatives2 = [a1, a2, a3, a4]
        
 
        decisionmatrix = DecisionMatrix(criteria2, alternatives2)
        
       # Create main pairwise matrix
        pairwise_matrix = np.array([[1, 2, 0.5],
                                    [0.5, 1, 1/3],
                                    [2, 3, 1]])
        
       # Create sub pairwise matrix for "Reliability"
        sub_pairwise_matrix_reliability = np.array([[1]])

        # Dictionary for sub pairwise matrices
        sub_pairwise_matrices = {'Reliability': sub_pairwise_matrix_reliability}
        
        
        ahp = AHP(decisionmatrix, pairwise_matrix, sub_pairwise_matrices)
        scores = ahp.calculate_ahp()
        print("AHP Scores:", scores)
        


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AHPTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
