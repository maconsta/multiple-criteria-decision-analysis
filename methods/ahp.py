import numpy as np
import core.core as core
from core.core import Pairwise


class AHP:
    def __init__(self, decision_matrix: core.DecisionMatrix, pairwise_matrix: np.ndarray, sub_pairwise_matrices=None):
        self.decision_matrix = decision_matrix
        self.pairwise_matrix = pairwise_matrix
        self.sub_pairwise_matrices = sub_pairwise_matrices if sub_pairwise_matrices else {}
        self.criteria_weights = self.calculate_criteria_weights()
        
    def calculate_sub_criteria_weights(self, criterion):
        if criterion.name in self.sub_pairwise_matrices:
            pairwise = Pairwise(len(criterion.sub_criteria))
            pairwise.P = self.sub_pairwise_matrices[criterion.name]
            return pairwise.Eigen_normalized()
        else:
            return np.ones(len(criterion.sub_criteria))

    def calculate_criteria_weights(self):
        #Initial criteria weights calculation
        pairwise = Pairwise(self.decision_matrix.crit_count)
        pairwise.P = self.pairwise_matrix
        initial_weights = pairwise.Eigen_normalized()

        #Sub criteria weights calculation
        final_weights = []
        for i, criterion in enumerate(self.decision_matrix.criteria):
            sub_weights = self.calculate_sub_criteria_weights(criterion)
            weighted_sub_weights = initial_weights[i] * sub_weights
            final_weights.extend(weighted_sub_weights)

        return np.array(final_weights)

    def weigh(self):
        for col in range(self.decision_matrix.normalized_matrix.shape[1]):
            self.decision_matrix.normalized_matrix[:, col] *= self.criteria_weights[col]

    def calculate_ahp(self):
        self.decision_matrix.normalize_l2()
        self.weigh()
        scores = np.sum(self.decision_matrix.normalized_matrix, axis=1)
        return scores
