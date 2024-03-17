#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from mcda.methods.topsis import Topsis
from mcda.core.core import Criterion, Alternative, DecisionMatrix


class TopsisCarTest (unittest.TestCase):
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

        decisionmatrix = DecisionMatrix(criteria2, alternatives2, DecisionMatrix.normalize)

        self.assertEqual(decisionmatrix.matrix[0][0], 7, "DM[0][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[0][1], 9, "DM[0][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[0][2], 9, "DM[0][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[0][3], 8, "DM[0][3] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][0], 8, "DM[1][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][1], 7, "DM[1][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][2], 8, "DM[1][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[1][3], 7, "DM[1][3] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][0], 9, "DM[2][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][1], 6, "DM[2][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][2], 8, "DM[2][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[2][3], 9, "DM[2][3] is not OK")
        self.assertEqual(decisionmatrix.matrix[3][0], 6, "DM[3][0] is not OK")
        self.assertEqual(decisionmatrix.matrix[3][1], 7, "DM[3][1] is not OK")
        self.assertEqual(decisionmatrix.matrix[3][2], 8, "DM[3][2] is not OK")
        self.assertEqual(decisionmatrix.matrix[3][3], 6, "DM[3][3] is not OK")

        # test topsis with linear normalizaton
        w = [0.1, 0.4, 0.4, 0.1]
        topsis = Topsis(decisionmatrix, w)
        topsis.weigh()
        topsis.calculate_ideal_solutions()

        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[0][0]), 0.078, 2, "M[0][0] is not OK")
        self.assertAlmostEqual(
            abs(topsis.decision_matrix.normalized_matrix[0][1]), 0.4, 2, "M[0][1] is not OK")
        self.assertAlmostEqual(
            abs(topsis.decision_matrix.normalized_matrix[0][2]), 0.4, 2, "M[0][2] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[0][3]), 0.089, 2, "M[0][3] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[1][0]), 0.089, 2, "M[1][0] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[1][1]), 0.312, 2, "M[1][1] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[1][2]), 0.356, 2, "M[1][2] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[1][3]), 0.078, 2, "M[1][3] is not OK")
        self.assertAlmostEqual(
            abs(topsis.decision_matrix.normalized_matrix[2][0]), 0.1, 2, "M[2][0] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[2][1]), 0.268, 2, "M[2][1] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[2][2]), 0.356, 2, "M[2][2] is not OK")
        self.assertAlmostEqual(
            abs(topsis.decision_matrix.normalized_matrix[2][3]), 0.1, 2, "M[2][3] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[3][0]), 0.067, 2, "M[3][0] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[3][1]), 0.312, 2, "M[3][1] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[3][2]), 0.356, 2, "M[3][2] is not OK")
        self.assertAlmostEqual(abs(
            topsis.decision_matrix.normalized_matrix[3][3]), 0.067, 2, "M[3][3] is not OK")

        self.assertAlmostEqual(abs(
            topsis.ideal_positive_solution[0]), 0.1, 2, "Positive ideal solution[0] is wrong")
        self.assertAlmostEqual(
            abs(topsis.ideal_positive_solution[1]), 0.4, 2, "Positive ideal[1] is wrong")
        self.assertAlmostEqual(
            abs(topsis.ideal_positive_solution[2]), 0.4, 2, "Positive ideal[2] is wrong")
        self.assertAlmostEqual(
            abs(topsis.ideal_positive_solution[3]), 0.067, 2, "Positive ideal[3] is wrong")

        self.assertAlmostEqual(abs(
            topsis.ideal_negative_solution[0]), 0.067, 2, "Negative ideal solution[0] is wrong")
        self.assertAlmostEqual(abs(
            topsis.ideal_negative_solution[1]), 0.268, 2, "Negative ideal solution[1] is wrong")
        self.assertAlmostEqual(abs(
            topsis.ideal_negative_solution[2]), 0.356, 2, "Negative ideal solution[2] is wrong")
        self.assertAlmostEqual(abs(
            topsis.ideal_negative_solution[3]), 0.1, 2, "Negative ideal solution[3] is wrong")

        pos_dist, neg_dist = topsis.calculate_distances()
        self.assertAlmostEqual(abs(
            pos_dist[0]), 0.03104207, 2, "Distance from positive ideal solution[0] is wrong")
        self.assertAlmostEqual(abs(
            pos_dist[1]), 0.1005791, 2, "Distance from positive ideal solution[1] is wrong")
        self.assertAlmostEqual(abs(
            pos_dist[2]), 0.144368, 2, "Distance from positive ideal solution[2] is wrong")
        self.assertAlmostEqual(abs(
            pos_dist[3]), 0.1048225, 2, "Distance from positive ideal solution[3] is wrong")

        self.assertAlmostEqual(abs(
            neg_dist[0]), 0.1399986, 2, "Distance from negative ideal solution[0] is wrong")
        self.assertAlmostEqual(abs(
            neg_dist[1]), 0.0532139, 2, "Distance from negative ideal solution[1] is wrong")
        self.assertAlmostEqual(abs(
            neg_dist[2]), 0.0330299, 2, "Distance from negative ideal solution[2] is wrong")
        self.assertAlmostEqual(abs(
            neg_dist[3]), 0.0544976, 2, "Distance from negative ideal solution[3] is wrong")

        closeness = topsis.calculate_closeness(pos_dist, neg_dist)
    
        self.assertAlmostEqual(
            abs(closeness[0]), 0.82, 1, "relative closeness to ideal solution[0] is wrong")
        self.assertAlmostEqual(
            abs(closeness[1]), 0.35, 1, "relative closeness to ideal solution[0] is wrong")
        self.assertAlmostEqual(
            abs(closeness[2]), 0.18, 1, "relative closeness to ideal solution[0] is wrong")
        self.assertAlmostEqual(
            abs(closeness[3]), 0.35, 1, "relative closeness to ideal solution[0] is wrong")


        # test topsis with l1 normalizaton
        # w = [0.1, 0.4, 0.4, 0.1]
        # topsis = Topsis(decisionmatrix, w)
        # topsis.decision_matrix.normalize_l1()
        # topsis.weigh()
        # topsis.calculate_ideal_solutions()

        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[0][0]), 0.023, 2, "M[0][0] is not OK")
        # self.assertAlmostEqual(
        #     abs(topsis.decision_matrix.normalized_matrix[0][1]), 0.12, 2, "M[0][1] is not OK")
        # self.assertAlmostEqual(
        #     abs(topsis.decision_matrix.normalized_matrix[0][2]), 0.11, 2, "M[0][2] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[0][3]), 0.027, 2, "M[0][3] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[1][0]), 0.027, 2, "M[1][0] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[1][1]), 0.097, 2, "M[1][1] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[1][2]), 0.097, 2, "M[1][2] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[1][3]), 0.023, 2, "M[1][3] is not OK")
        # self.assertAlmostEqual(
        #     abs(topsis.decision_matrix.normalized_matrix[2][0]), 0.03, 2, "M[2][0] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[2][1]), 0.083, 2, "M[2][1] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[2][2]), 0.097, 2, "M[2][2] is not OK")
        # self.assertAlmostEqual(
        #     abs(topsis.decision_matrix.normalized_matrix[2][3]), 0.03, 2, "M[2][3] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[3][0]), 0.02, 2, "M[3][0] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[3][1]), 0.097, 2, "M[3][1] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[3][2]), 0.097, 2, "M[3][2] is not OK")
        # self.assertAlmostEqual(abs(
        #     topsis.decision_matrix.normalized_matrix[3][3]), 0.023, 2, "M[3][3] is not OK")

        # self.assertAlmostEqual(abs(
        #     topsis.ideal_positive_solution[0]), 0.03, 2, "Positive ideal solution[0] is wrong")
        # self.assertAlmostEqual(
        #     abs(topsis.ideal_positive_solution[1]), 0.12, 2, "Positive ideal[1] is wrong")
        # self.assertAlmostEqual(
        #     abs(topsis.ideal_positive_solution[2]), 0.11, 2, "Positive ideal[2] is wrong")
        # self.assertAlmostEqual(
        #     abs(topsis.ideal_positive_solution[3]), 0.023, 2, "Positive ideal[3] is wrong")

        # self.assertAlmostEqual(abs(
        #     topsis.ideal_negative_solution[0]), 0.023, 2, "Negative ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(
        #     topsis.ideal_negative_solution[1]), 0.083, 2, "Negative ideal solution[1] is wrong")
        # self.assertAlmostEqual(abs(
        #     topsis.ideal_negative_solution[2]), 0.097, 2, "Negative ideal solution[2] is wrong")
        # self.assertAlmostEqual(abs(
        #     topsis.ideal_negative_solution[3]), 0.03, 2, "Negative ideal solution[3] is wrong")

        # pos_dist, neg_dist = topsis.calculate_distances()
        # self.assertAlmostEqual(abs(
        #     pos_dist[0]), 0.01, 2, "Distance from positive ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(
        #     pos_dist[1]), 0.03, 2, "Distance from positive ideal solution[1] is wrong")
        # self.assertAlmostEqual(abs(
        #     pos_dist[2]), 0.04, 2, "Distance from positive ideal solution[2] is wrong")
        # self.assertAlmostEqual(abs(
        #     pos_dist[3]), 0.03, 2, "Distance from positive ideal solution[3] is wrong")

        # self.assertAlmostEqual(abs(
        #     neg_dist[0]), 0.04, 2, "Distance from negative ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(
        #     neg_dist[1]), 0.02, 2, "Distance from negative ideal solution[1] is wrong")
        # self.assertAlmostEqual(abs(
        #     neg_dist[2]), 0.01, 2, "Distance from negative ideal solution[2] is wrong")
        # self.assertAlmostEqual(abs(
        #     neg_dist[3]), 0.02, 2, "Distance from negative ideal solution[3] is wrong")

        # closeness = topsis.calculate_closeness(pos_dist, neg_dist)

        # self.assertAlmostEqual(
        #     abs(closeness[0]), 0.82, 1, "relative closeness to ideal solution[0] is wrong")
        # self.assertAlmostEqual(
        #     abs(closeness[1]), 0.35, 1, "relative closeness to ideal solution[0] is wrong")
        # self.assertAlmostEqual(
        #     abs(closeness[2]), 0.18, 1, "relative closeness to ideal solution[0] is wrong")
        # self.assertAlmostEqual(
        #     abs(closeness[3]), 0.35, 1, "relative closeness to ideal solution[0] is wrong")


        # test topsis with l2 normalization
        # w = [0.1, 0.4, 0.4, 0.2]
        # topsis = Topsis(decisionmatrix, w)
        # topsis.decision_matrix.normalize_l2()
        # topsis.weigh()
        # topsis.calculate_ideal_solutions()

        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[0][0]), 0.046, 2, "M[0][0] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[0][1]), 0.244, 2, "M[0][1] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[0][2]), 0.216, 2, "M[0][2] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[0][3]), 0.106, 2, "M[0][3] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[1][0]), 0.053, 2, "M[1][0] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[1][1]), 0.192, 2, "M[1][1] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[1][2]), 0.192, 2, "M[1][2] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[1][3]), 0.092, 2, "M[1][3] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[2][0]), 0.059, 2, "M[2][0] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[2][1]), 0.164, 2, "M[2][1] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[2][2]), 0.192, 2, "M[2][2] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[2][3]), 0.118, 2, "M[2][3] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[3][0]), 0.040, 2, "M[3][0] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[3][1]), 0.192, 2, "M[3][1] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[3][2]), 0.192, 2, "M[3][2] is not OK")
        # self.assertAlmostEqual(abs(topsis.decision_matrix.normalized_matrix[3][3]), 0.080, 2, "M[3][3] is not OK")

        # self.assertAlmostEqual(abs(topsis.ideal_positive_solution[0]),0.059,2,"Positive ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(topsis.ideal_positive_solution[1]),0.244,2,"Positive ideal[1] is wrong")
        # self.assertAlmostEqual(abs(topsis.ideal_positive_solution[2]),0.216,2,"Positive ideal[2] is wrong")
        # self.assertAlmostEqual(abs(topsis.ideal_positive_solution[3]),0.080,2,"Positive ideal[3] is wrong")

        # self.assertAlmostEqual(abs(topsis.ideal_negative_solution[0]),0.04,2,"Negative ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(topsis.ideal_negative_solution[1]),0.164,2,"Negative ideal solution[1] is wrong")
        # self.assertAlmostEqual(abs(topsis.ideal_negative_solution[2]),0.192,2,"Negative ideal solution[2] is wrong")
        # self.assertAlmostEqual(abs(topsis.ideal_negative_solution[3]),0.118,2,"Negative ideal solution[3] is wrong")

        # pos_dist, neg_dist = topsis.calculate_distances()
        # self.assertAlmostEqual(abs(pos_dist[0]),0.029,2,"Distance from positive ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(pos_dist[1]),0.057,2,"Distance from positive ideal solution[1] is wrong")
        # self.assertAlmostEqual(abs(pos_dist[2]),0.090,2,"Distance from positive ideal solution[2] is wrong")
        # self.assertAlmostEqual(abs(pos_dist[3]),0.058,2,"Distance from positive ideal solution[3] is wrong")

        # self.assertAlmostEqual(abs(neg_dist[0]),0.083,2,"Distance from negative ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(neg_dist[1]),0.040,2,"Distance from negative ideal solution[1] is wrong")
        # self.assertAlmostEqual(abs(neg_dist[2]),0.019,2,"Distance from negative ideal solution[2] is wrong")
        # self.assertAlmostEqual(abs(neg_dist[3]),0.047,2,"Distance from negative ideal solution[3] is wrong")

        # closeness = topsis.calculate_closeness(pos_dist, neg_dist)

        # self.assertAlmostEqual(abs(closeness[0]),0.74,1,"relative closeness to ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(closeness[1]),0.41,1,"relative closeness to ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(closeness[2]),0.17,1,"relative closeness to ideal solution[0] is wrong")
        # self.assertAlmostEqual(abs(closeness[3]),0.45,1,"relative closeness to ideal solution[0] is wrong")


        # uncomment for testing
        # test = topsis.calculate_topsis()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TopsisCarTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
