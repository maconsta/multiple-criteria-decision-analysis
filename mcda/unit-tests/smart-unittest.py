import unittest
from mcda.methods.smart import SMART
from mcda.core.core import Criterion, Alternative, DecisionMatrix

class SmartCarTest (unittest.TestCase):
     def runTest(self):
        c1 = Criterion("c1", "max")
        c2 = Criterion("c2", "max")
        c3 = Criterion("c3", "max")
        c4 = Criterion("c4", "max")
        c5 = Criterion("c5", "max")
        c6 = Criterion("c6", "max")
        criteria = [c1, c2, c3, c4, c5, c6]

        a1 = Alternative("a1", [1350, 1850, 7.5, 2.58, 93.5, 0.045])
        a2 = Alternative("a2", [1680, 1650, 8.5, 3.75, 95.3, 0.068])
        a3 = Alternative("a3", [1560, 1950, 6.5, 4.86, 88.6, 0.095])
        a4 = Alternative("a4", [1470, 1850, 9.5, 3.16, 98.4, 0.072])
        alternatives = [a1, a2, a3, a4]

        dm = DecisionMatrix(criteria, alternatives, DecisionMatrix.normalize_l2)
        weights = [0.2336, 0.1652, 0.3355, 0.1021, 0.0424, 0.1212] # using pre-calculated weights

        smart = SMART(dm, weights)
        smart.calculate_electre() # normalized with L2 normalization

        # test normalized weighted matrix
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[0][0]), 0.10374919, 3,"M[0][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[0][1]), 0.08358264, 3,"M[0][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[0][2]), 0.15575196, 3,"M[0][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[0][3]), 0.03573956, 3,"M[0][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[0][4]), 0.0210834, 3,"M[0][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[0][5]), 0.03776407, 3,"M[0][5] in Normalized Weighted Matrix 'M' is not okay")

        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[1][0]), 0.12911011, 3,"M[1][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[1][1]), 0.07454668, 3,"M[1][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[1][2]), 0.17651889, 3,"M[1][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[1][3]), 0.05194703, 3,"M[1][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[1][4]), 0.02148928, 3,"M[1][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[1][5]), 0.05706571, 3,"M[1][5] in Normalized Weighted Matrix 'M' is not okay")
       
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[2][0]), 0.11988795, 3,"M[2][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[2][1]), 0.08810062, 3,"M[2][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[2][2]), 0.13498504, 3,"M[2][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[2][3]), 0.06732335, 3,"M[2][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[2][4]), 0.01997849, 3,"M[2][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[2][5]), 0.07972415, 3,"M[2][5] in Normalized Weighted Matrix 'M' is not okay")

        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[3][0]), 0.11297134, 3,"M[3][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[3][1]), 0.08358264, 3,"M[3][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[3][2]), 0.19728582, 3,"M[3][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[3][3]), 0.04377403, 3,"M[3][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[3][4]), 0.0221883, 3,"M[3][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(smart.decision_matrix.normalized_matrix[3][5]), 0.06042251, 3,"M[3][5] in Normalized Weighted Matrix 'M' is not okay")
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(SmartCarTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
