import unittest
import numpy as np
from methods.ahp import AHP
from core.core import Criterion, Alternative, DecisionMatrix

class AHPTest(unittest.TestCase):
    def runTest(self):
        c1 = Criterion("style", "max")
        c2 = Criterion("reliability", "max")
        c3 = Criterion("economy", "max")
        c4 = Criterion("price", "min")
        criteria2 = [c1, c2, c3, c4]
        
        a1 = Alternative("Honda", [7, 9, 9, 8])
        a2 = Alternative("Saturn", [8, 7, 8, 7])
        a3 = Alternative("Ford", [9, 6, 8, 9])
        a4 = Alternative("Mazda", [6, 7, 8, 6])
        alternatives2 = [a1, a2, a3, a4]
        
        
        decision_matrix = DecisionMatrix(criteria2, alternatives2)
        
        # Pairwise comparison matrix based on user judgment
        pairwise_matrix = np.array([[1, 0.5, 2, 0.7], [2, 1, 3, 1.5], [0.5, 1/3, 1, 0.4], [1.4, 0.67, 2.5, 1]])
        
        ahp = AHP(decision_matrix, pairwise_matrix)
        
        # Check if criteria_weights were calculated correctly
        # expected_criteria_weights = np.array([x, x, x])  # Replace with actual expected values
        # np.testing.assert_array_almost_equal(ahp.criteria_weights, expected_criteria_weights, decimal=1)
        
        
        scores = ahp.calculate_ahp()
        print(scores)
        # expected_scores = np.array([x, x, x])  # Replace with actual expected values
        # np.testing.assert_array_almost_equal(scores, expected_scores, decimal=1)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(AHPTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
