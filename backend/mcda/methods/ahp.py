import numpy as np
import backend.mcda.core.core as core


class AHP:
    def __init__(self, decision_matrix: core.DecisionMatrix, weights):
        self.decision_matrix = decision_matrix
        self.weights = weights

    def weigh(self):
        self.decision_matrix.normalized_matrix *= self.weights

        # print("Weighted Normalized Matrix:\n",
        #       self.decision_matrix.normalized_matrix)  # Print the weighted normalized matrix

    def calculate_scores(self):
        scores = np.sum(self.decision_matrix.normalized_matrix, axis=1)
        # print("Calculated Scores:", scores)  # Print the calculated scores
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

        return result

# Some tests, will delete later
# c1 = core.Criterion("style", "max")
# c2 = core.Criterion("reliability", "max")
# c3 = core.Criterion("economy", "max")
# c4 = core.Criterion("price", "min")
# criteria2 = [c1, c2, c3, c4]
#
# a1 = core.Alternative("Honda", [7, 9, 9, 8])
# a2 = core.Alternative("Saturn", [8, 7, 8, 7])
# a3 = core.Alternative("Ford", [9, 6, 8, 9])
# a4 = core.Alternative("Mazda", [6, 7, 8, 6])
# alternatives2 = [a1, a2, a3, a4]
#
# dm = core.DecisionMatrix(criteria2, alternatives2, core.DecisionMatrix.normalize_l2)
# ahp = AHP(decision_matrix=dm, weights=[0.218, 0.149, 0.1018, 0.5312])
# print(ahp.calculate_ahp())