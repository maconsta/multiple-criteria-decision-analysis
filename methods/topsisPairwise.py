
import numpy as np
from core.core import DecisionMatrix, Pairwise
from methods.topsis import Topsis

# ---------------------------------------------CLASS_TOPSIS_PAIRWISE_START---------------------------------------------------
class TopsisPairwise:
    def __init__(self, decision_matrix: DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights

    def calculate_topsisPairwise(self):
        self.decision_matrix.normalize()
        weighted_normalized_matrix = self.decision_matrix.normalized_matrix * self.weights
        
        ideal_positive = np.max(weighted_normalized_matrix, axis=0)
        ideal_negative = np.min(weighted_normalized_matrix, axis=0)

        positive_distances = np.linalg.norm(weighted_normalized_matrix - ideal_positive, axis=1)
        negative_distances = np.linalg.norm(weighted_normalized_matrix - ideal_negative, axis=1)

        scores = negative_distances / (negative_distances + positive_distances)
        best_alternative_index = np.argmax(scores)

        return scores, self.decision_matrix.alternatives[best_alternative_index].name, best_alternative_index
# ---------------------------------------------CLASS_TOPSIS_PAIRWISE_END------------------------------------------------------

# Run the file from the console: python -m methods.topsisPairwise
# or there will be an error

#weights = [0.232, 0.402, 0.061, 0.305]

#dm = DecisionMatrix(crit_count=4, alt_count=3)
#dm.set_alternative(0, [0.751, 0.480, 0.077, 0.066])
#dm.set_alternative(1, [0.178, 0.406, 0.231, 0.615])
#dm.set_alternative(2, [0.071, 0.114, 0.692, 0.319])

#pw = TopsisPairwise(dm, weights)

#closeness, best_alternative_index, best_alternative_closeness = pw.calculate_topsis()

#print("Closeness:")
#print(closeness)

#print("Best Alternative Index:", best_alternative_index + 1)
