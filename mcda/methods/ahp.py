import numpy as np
import core.core as core

class AHP:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights):
        self.decision_matrix = decision_matrix
        self.weights = weights


    def weigh(self):
        for col in range(self.decision_matrix.normalized_matrix.shape[0]):
            self.decision_matrix.normalized_matrix[:, col] *= self.weights[col]
        print("Weighted Normalized Matrix:\n", self.decision_matrix.normalized_matrix)  # Print the weighted normalized matrix

    def calculate_scores(self):
        scores = np.sum(self.decision_matrix.normalized_matrix, axis=1)
        print("Calculated Scores:", scores)  # Print the calculated scores
        return scores

    def calculate_ahp(self):
        # Assuming normalization is already applied during DecisionMatrix initialization
        # No need to normalize again here, if normalization is chosen to be applied externally
        self.weigh()
        scores = self.calculate_scores()

        result = []
        for i in range(len(scores)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": scores[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)
        print("Final Result:", result)  # Print the final result
        return result
