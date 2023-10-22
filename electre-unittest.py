import unittest
from methods.electre import Electre 
from core.core import Criterion, Alternative, DecisionMatrix


class ElectreTest(unittest.TestCase):
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

        dm = DecisionMatrix(criteria, alternatives)
        weights = [0.2336, 0.1652, 0.3355, 0.1021, 0.0424, 0.1212] # using pre-calculated weights

        el = Electre(dm, weights)
        el.calculate_electre() # normalized with L2 normalization

        # test normalized weighted matrix
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[0][0]), 0.10374919, 3,"M[0][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[0][1]), 0.08358264, 3,"M[0][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[0][2]), 0.15575196, 3,"M[0][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[0][3]), 0.03573956, 3,"M[0][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[0][4]), 0.0210834, 3,"M[0][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[0][5]), 0.03776407, 3,"M[0][5] in Normalized Weighted Matrix 'M' is not okay")

        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[1][0]), 0.12911011, 3,"M[1][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[1][1]), 0.07454668, 3,"M[1][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[1][2]), 0.17651889, 3,"M[1][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[1][3]), 0.05194703, 3,"M[1][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[1][4]), 0.02148928, 3,"M[1][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[1][5]), 0.05706571, 3,"M[1][5] in Normalized Weighted Matrix 'M' is not okay")
       
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[2][0]), 0.11988795, 3,"M[2][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[2][1]), 0.08810062, 3,"M[2][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[2][2]), 0.13498504, 3,"M[2][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[2][3]), 0.06732335, 3,"M[2][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[2][4]), 0.01997849, 3,"M[2][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[2][5]), 0.07972415, 3,"M[2][5] in Normalized Weighted Matrix 'M' is not okay")

        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[3][0]), 0.11297134, 3,"M[3][0] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[3][1]), 0.08358264, 3,"M[3][1] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[3][2]), 0.19728582, 3,"M[3][2] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[3][3]), 0.04377403, 3,"M[3][3] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[3][4]), 0.0221883, 3,"M[3][4] in Normalized Weighted Matrix 'M' is not okay")
        self.assertAlmostEqual(abs(el.decision_matrix.normalized_matrix[3][5]), 0.06042251, 3,"M[3][5] in Normalized Weighted Matrix 'M' is not okay")
        
        # test concordance interval matrix
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[0][0]), 0, 3,"C[0][0] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[0][1]), 0.1652, 3,"C[0][1] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[0][2]), 0.3779, 3,"C[0][2] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[0][3]), 0.1652, 3,"C[0][3] in Concordance Interval Matrix 'C' is not okay")

        self.assertAlmostEqual(abs(el.concordance_interval_matrix[1][0]), 0.8348, 3,"C[1][0] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[1][1]), 0, 3,"C[1][1] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[1][2]), 0.6115, 3,"C[1][2] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[1][3]), 0.3357, 3,"C[1][3] in Concordance Interval Matrix 'C' is not okay")

        self.assertAlmostEqual(abs(el.concordance_interval_matrix[2][0]), 0.6221, 3,"C[2][0] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[2][1]), 0.3885, 3,"C[2][1] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[2][2]), 0, 3,"C[2][2] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[2][3]), 0.6221, 3,"C[2][3] in Concordance Interval Matrix 'C' is not okay")

        self.assertAlmostEqual(abs(el.concordance_interval_matrix[3][0]), 1, 3,"C[3][0] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[3][1]), 0.6643, 3,"C[3][1] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[3][2]), 0.3779, 3,"C[3][2] in Concordance Interval Matrix 'C' is not okay")
        self.assertAlmostEqual(abs(el.concordance_interval_matrix[3][3]), 0, 3,"C[3][3] in Concordance Interval Matrix 'C' is not okay")
        
        # test concordance index matrix
        self.assertAlmostEqual(abs(el.concordance_index_matrix[0][0]), 0, 3,"F[0][0] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[0][1]), 0, 3,"F[0][1] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[0][2]), 0, 3,"F[0][2] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[0][3]), 0, 3,"F[0][3] in Concordance Index Matrix 'F' is not okay")

        self.assertAlmostEqual(abs(el.concordance_index_matrix[1][0]), 1, 3,"F[1][0] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[1][1]), 0, 3,"F[1][1] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[1][2]), 1, 3,"F[1][2] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[1][3]), 0, 3,"F[1][3] in Concordance Index Matrix 'F' is not okay")

        self.assertAlmostEqual(abs(el.concordance_index_matrix[2][0]), 1, 3,"F[2][0] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[2][1]), 0, 3,"F[2][1] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[2][2]), 0, 3,"F[2][2] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[2][3]), 1, 3,"F[2][3] in Concordance Index Matrix 'F' is not okay")

        self.assertAlmostEqual(abs(el.concordance_index_matrix[3][0]), 1, 3,"F[3][0] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[3][1]), 1,3, "F[3][1] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[3][2]), 0,3, "F[3][2] in Concordance Index Matrix 'F' is not okay")
        self.assertAlmostEqual(abs(el.concordance_index_matrix[3][3]), 0, 3,"F[3][3] in Concordance Index Matrix 'F' is not okay")

        # test discordance interval matrix
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[0][0]), 0, 3,"D[0][0] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[0][1]), 1, 3,"D[0][1] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[0][2]), 1, 3,"D[0][2] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[0][3]), 1, 3,"D[0][3] in Discordance Interval Matrix 'D' is not okay")

        self.assertAlmostEqual(abs(el.discordance_interval_matrix[1][0]), 0.35629477, 3,"D[1][0] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[1][1]), 0, 3,"D[1][1] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[1][2]), 0.54554149, 3,"D[1][2] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[1][3]), 1, 3,"D[1][3] in Discordance Interval Matrix 'D' is not okay")

        self.assertAlmostEqual(abs(el.discordance_interval_matrix[2][0]), 0.49492111, 3,"D[2][0] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[2][1]), 1, 3,"D[2][1] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[2][2]), 0, 3,"D[2][2] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[2][3]), 1, 3,"D[2][3] in Discordance Interval Matrix 'D' is not okay")

        self.assertAlmostEqual(abs(el.discordance_interval_matrix[3][0]), 0, 3,"D[3][0] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[3][1]), 0.7771377, 3,"D[3][1] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[3][2]), 0.37799397, 3,"D[3][2] in Discordance Interval Matrix 'D' is not okay")
        self.assertAlmostEqual(abs(el.discordance_interval_matrix[3][3]), 0, 3,"D[3][3] in Discordance Interval Matrix 'D' is not okay")
        
        # test discordance index matrix
        self.assertAlmostEqual(abs(el.discordance_index_matrix[0][0]), 1, 3,"G[0][0] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[0][1]), 0, 3,"G[0][1] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[0][2]), 0, 3,"G[0][2] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[0][3]), 0, 3,"G[0][3] in Discordance Index Matrix 'G' is not okay")

        self.assertAlmostEqual(abs(el.discordance_index_matrix[1][0]), 1, 3,"G[1][0] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[1][1]), 1, 3,"G[1][1] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[1][2]), 1, 3,"G[1][2] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[1][3]), 0, 3,"G[1][3] in Discordance Index Matrix 'G' is not okay")

        self.assertAlmostEqual(abs(el.discordance_index_matrix[2][0]), 1, 3,"G[2][0] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[2][1]), 0, 3,"G[2][1] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[2][2]), 1, 3,"G[2][2] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[2][3]), 0, 3,"G[2][3] in Discordance Index Matrix 'G' is not okay")

        self.assertAlmostEqual(abs(el.discordance_index_matrix[3][0]), 1, 3,"G[3][0] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[3][1]), 0, 3,"G[3][1] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[3][2]), 1, 3,"G[3][2] in Discordance Index Matrix 'G' is not okay")
        self.assertAlmostEqual(abs(el.discordance_index_matrix[3][3]), 1, 3,"G[3][3] in Discordance Index Matrix 'G' is not okay")

        # test net superior vector
        self.assertAlmostEqual(abs(el.net_superior_vector[0]), 1.7486, 3,"V[0] in Net Superior Vector 'V' is not okay")
        self.assertAlmostEqual(abs(el.net_superior_vector[1]), 0.564, 3,"V[1] in Net Superior Vector 'V' is not okay")
        self.assertAlmostEqual(abs(el.net_superior_vector[2]), 0.2654, 3,"V[2] in Net Superior Vector 'V' is not okay")
        self.assertAlmostEqual(abs(el.net_superior_vector[3]), 0.9192, 3,"V[3] in Net Superior Vector 'V' is not okay")

        # test net inferior vector
        self.assertAlmostEqual(abs(el.net_inferior_vector[0]), 2.14878413, 3,"U[0] in Net Superior Vector 'U' is not okay")
        self.assertAlmostEqual(abs(el.net_inferior_vector[1]), 0.87530144, 3,"U[1] in Net Superior Vector 'U' is not okay")
        self.assertAlmostEqual(abs(el.net_inferior_vector[2]), 0.57138565, 3,"U[2] in Net Superior Vector 'U' is not okay")
        self.assertAlmostEqual(abs(el.net_inferior_vector[3]), 1.84486833, 3,"U[3] in Net Superior Vector 'U' is not okay")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ElectreTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
