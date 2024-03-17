import unittest
from mcda.methods.ahp import AHP
from mcda.core.core import Criterion, Alternative, DecisionMatrix, Pairwise


class AHPTest(unittest.TestCase):
    def runTest(self):
        # Criteria and alternatives setup
        c1 = Criterion("criteria1", "max")
        c2 = Criterion("criteria2", "max")
        criteria = [c1, c2]

        a1 = Alternative("Alternative1", [1, 2])
        a2 = Alternative("Alternative2", [3, 4])
        alternatives = [a1, a2]

        decision_matrix = DecisionMatrix(criteria, alternatives)

        # Pairwise matrix setup
        pairwise_matrix = Pairwise(criteria)
        pairwise_matrix.pairwise_matrix = np.array([[1, 2], [0.5, 1]])  # Example pairwise matrix

        ahp = AHP(decision_matrix, pairwise_matrix)

        # Test normalization
        ahp.decision_matrix.normalize_l2()
        normalized_matrix = ahp.decision_matrix.normalized_matrix
        expected_normalized = np.array([[0.31622777, 0.4472136], [0.9486833, 0.89442719]])
        np.testing.assert_almost_equal(normalized_matrix, expected_normalized, decimal=5, 
                                       err_msg="Normalization failed")

        # Test weight calculation
        ahp.calculate_weights()
        expected_weights = np.array([0.66666667, 0.33333333])
        np.testing.assert_almost_equal(ahp.weights, expected_weights, decimal=5, 
                                       err_msg="Weight calculation failed")

        '''
        # Test scoring
        scores = ahp.calculate_scores()
        print("Scores generated in test:", scores)  # Add this print statement
        expected_scores = np.array([0.35988971, 0.93059793])
        np.testing.assert_almost_equal(scores, expected_scores, decimal=5, 
                               err_msg="Scoring failed")
        '''

        # Test final result
        results = ahp.calculate_ahp()
        expected_results = [{'name': 'Alternative2', 'score': 0.93059793}, 
                            {'name': 'Alternative1', 'score': 0.35988971}]
        self.assertEqual(results, expected_results, "AHP final result failed")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AHPTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
