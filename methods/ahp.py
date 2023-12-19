import numpy as np
import core.core as core

class AHP:
    def __init__(self, decision_matrix: core.DecisionMatrix, pairwise_matrix: core.Pairwise):
        self.decision_matrix = decision_matrix
        self.pairwise_matrix = pairwise_matrix
        self.weights = None

    def calculate_weights(self):
        # Use the Pairwise object to calculate the eigenvector
        self.weights = self.pairwise_matrix.calculate_eigenvector()
        print("Calculated Weights:", self.weights)  # Print the calculated weights

    def weigh(self):
        for col in range(self.decision_matrix.normalized_matrix.shape[1]):
            self.decision_matrix.normalized_matrix[:, col] *= self.weights[col]
        print("Weighted Normalized Matrix:\n", self.decision_matrix.normalized_matrix)  # Print the weighted normalized matrix

    def calculate_scores(self):
        scores = np.sum(self.decision_matrix.normalized_matrix, axis=1)
        print("Calculated Scores:", scores)  # Print the calculated scores
        return scores

    def calculate_ahp(self):
        self.decision_matrix.normalize_l2()
        print("Normalized Matrix in calculate_ahp:\n", self.decision_matrix.normalized_matrix)
        self.calculate_weights()
        self.weigh()
        print("Weighted Normalized Matrix in calculate_ahp:\n", self.decision_matrix.normalized_matrix)
        scores = self.calculate_scores()
        print("Scores in calculate_ahp:", scores)

        result = []
        for i in range(len(scores)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": scores[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)
        print("Final Result:", result)  # Print the final result
        return result


