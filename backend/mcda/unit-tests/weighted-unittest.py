#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from backend.mcda.methods.weightedSum import WeightedSum
from backend.mcda.core.core import Criterion, Alternative, DecisionMatrix


class WeightedSumTest (unittest.TestCase):
    def runTest (self):
        c1 = Criterion("expense","max")
        c2 = Criterion("operability","max")
        c3 = Criterion("reliability","max")
        c4 = Criterion("flexibility","max")
        criteria2 = [c1,c2,c3,c4]
        
        a1 = Alternative("X", [0.751,0.480, 0.077,0.066])
        a2 = Alternative("Y", [0.178,0.406,0.231,0.615])
        a3 = Alternative("Z", [0.071,0.114,0.692,0.319])
        w = [0.232, 0.402, 0.061, 0.305]
        alternatives2 = [a1, a2, a3]
        decisionmatrix = DecisionMatrix(criteria2, alternatives2, DecisionMatrix.normalize_l2)        

        self.assertEqual(decisionmatrix.matrix[0][0], 0.751, "DM[0][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[0][1], 0.480, "DM[0][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[0][2], 0.077, "DM[0][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[0][3], 0.066, "DM[0][3] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][0], 0.178, "DM[1][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][1], 0.406, "DM[1][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][2], 0.231, "DM[1][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][3], 0.615, "DM[1][3] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][0], 0.071, "DM[2][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][1], 0.114, "DM[2][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][2], 0.692, "DM[2][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][3], 0.319, "DM[2][3] is not OK")
        
        # wh = WeightedSum(decisionmatrix, w)
        # wh.calculate_weighted_sum()
        # ADD TESTS FOR THE RESULT OF WH.CALCULATE_WEIGHTED_SUM

        


def suite():
    suite = unittest.TestSuite()
    suite.addTest (WeightedSumTest())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)

