import numpy as np
import core.core as core 

class AHP: 
    def __init__ (self, decision_matrix: core.DecisionMatrix, pairwise_matrix: np.ndarray):
        self.decision_matrix = decision_matrix
        self.pairwise_matrix = pairwise_matrix
        self.criteria_weights = self.calculate_criteria_weights()
        
    
    def calculate_criteria_weights(self):
        pairwise = core.Pairwise(self.decision_matrix.crit_count)
        pairwise.P = self.pairwise_matrix
        return pairwise.Eigen()
    
    
    def weigh(self):
        for col in range(self.decision_matrix.normalized_matrix.shape[1]):
            self.decision_matrix.normalized_matrix[:, col] *= self.criteria_weights[col]
    
    def calculate_ahp(self):
        self.decision_matrix.normalize_l2()
        self.weigh()
        scores = np.sum(self.decision_matrix.normalized_matrix, axis=1)
        return scores