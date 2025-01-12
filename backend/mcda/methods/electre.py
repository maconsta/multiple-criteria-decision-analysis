import numpy as np
from backend.mcda.core.core import Criterion, Alternative, DecisionMatrix


class Electre:
    def __init__(self, decision_matrix: DecisionMatrix, weights):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.concordance_interval_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.concordance_index_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.discordance_interval_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.discordance_index_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.net_superior_vector = np.zeros(self.decision_matrix.alt_count)
        self.net_inferior_vector = np.zeros(self.decision_matrix.alt_count)
        self.average_ranking_vector = []

    def weigh(self):
        self.decision_matrix.normalized_matrix *= self.weights

    def calculate_concordance_interval_matrix(self):
        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if i == j:
                    continue

                for k in range(self.decision_matrix.crit_count):
                    if self.decision_matrix.normalized_matrix[i][k] >= self.decision_matrix.normalized_matrix[j][k]:
                        self.concordance_interval_matrix[i][j] += self.weights[k]

    def calculate_concordance_index_matrix(self):
        col_sums = np.sum(self.concordance_interval_matrix, axis=0)
        c_threshold = np.sum(col_sums) / (
                self.decision_matrix.alt_count * (self.decision_matrix.alt_count - 1))

        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if i == j:
                    continue
                if self.concordance_interval_matrix[i][j] >= c_threshold:
                    self.concordance_index_matrix[i][j] = 1
                else:
                    self.concordance_index_matrix[i][j] = 0

    def calculate_discordance_interval_matrix(self):
        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if i == j:
                    continue

                abs_vector = []
                discordance_abs_vector = []
                for k in range(self.decision_matrix.crit_count):
                    abs_vector.append(abs(
                        self.decision_matrix.normalized_matrix[i][k] - self.decision_matrix.normalized_matrix[j][k]))

                    if self.decision_matrix.normalized_matrix[i][k] < self.decision_matrix.normalized_matrix[j][k]:
                        (discordance_abs_vector.append(abs(
                            self.decision_matrix.normalized_matrix[i][k] - self.decision_matrix.normalized_matrix[j][
                                k])))

                for k in range(self.decision_matrix.crit_count):
                    if self.decision_matrix.normalized_matrix[i][k] < self.decision_matrix.normalized_matrix[j][k]:
                        self.discordance_interval_matrix[i][j] = max(discordance_abs_vector) / max(abs_vector)

    def calculate_discordance_index_matrix(self):
        col_sums = np.sum(self.discordance_interval_matrix, axis=0)
        d_threshold = np.sum(col_sums) / (
                self.decision_matrix.alt_count * (self.decision_matrix.alt_count - 1))

        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if i == j:
                    continue
                if self.discordance_interval_matrix[i][j] < d_threshold:
                    self.discordance_index_matrix[i][j] = 1
                else:
                    self.discordance_index_matrix[i][j] = 0

    def calculate_net_superior_vector(self):
        col_sums = np.sum(self.concordance_interval_matrix, axis=0)
        row_sums = np.sum(self.concordance_interval_matrix, axis=1)

        self.net_superior_vector = row_sums - col_sums

    def calculate_net_inferior_vector(self):
        col_sums = np.sum(self.discordance_interval_matrix, axis=0)
        row_sums = np.sum(self.discordance_interval_matrix, axis=1)

        self.net_inferior_vector = row_sums - col_sums

    def calculate_average_ranking_vector(self):
        superior_ranking = []
        inferior_ranking = []

        for i in range(len(self.net_superior_vector)):
            name = self.decision_matrix.alternatives[i].name
            superior_ranking.append({"name": name, "score": self.net_superior_vector[i]})
        superior_ranking = sorted(superior_ranking, key=lambda d: d['score'], reverse=True)

        for i in range(len(self.net_inferior_vector)):
            name = self.decision_matrix.alternatives[i].name
            inferior_ranking.append({"name": name, "score": self.net_inferior_vector[i]})
        inferior_ranking = sorted(inferior_ranking, key=lambda d: d['score'])

        for i in range(len(superior_ranking)):
            for j in range(len(inferior_ranking)):
                if superior_ranking[i]["name"] == inferior_ranking[j]["name"]:
                    rank_i = i + 1
                    rank_j = j + 1
                    avg_rank = int((rank_i + rank_j) / 2)
                    self.average_ranking_vector.append({"name": superior_ranking[i]["name"], "averange_rank": avg_rank})

        self.average_ranking_vector = sorted(self.average_ranking_vector, key=lambda d: d['averange_rank'])

    def calculate_electre(self):
        print("\n???")
        print("\nNormalized DM")
        print(self.decision_matrix.normalized_matrix)

        self.weigh()
        print("\nNormalized Weighted DM")
        print(self.decision_matrix.normalized_matrix)

        self.calculate_concordance_interval_matrix()
        print("\nConcordance Interval Matrix")
        print(self.concordance_interval_matrix)

        self.calculate_concordance_index_matrix()
        print("\nConcordance Index Matrix")
        print(self.concordance_index_matrix)

        self.calculate_discordance_interval_matrix()
        print("\nDiscordance Interval Matrix")
        print(self.discordance_interval_matrix)

        self.calculate_discordance_index_matrix()
        print("\nDiscordance Index Matrix")
        print(self.discordance_index_matrix)

        self.calculate_net_superior_vector()
        print("\nNet Superior Vector")
        print(self.net_superior_vector)

        self.calculate_net_inferior_vector()
        print("\nNet Inferior Vector")
        print(self.net_inferior_vector)

        self.calculate_average_ranking_vector()
        print("\nAverage Ranking Vector")
        print(self.average_ranking_vector)

        return self.average_ranking_vector


# TEST TAKEN FROM https://www.academia.edu/17051534/APPLICATION_OF_ELECTRE_II
# c1 = Criterion("price", "max")
# c2 = Criterion("technique", "max")
# c3 = Criterion("BQ", "max")
# c4 = Criterion("mc", "max")
#
# criteria = [c1, c2, c3, c4]
#
# a1 = Alternative("a1", [2330, 12.8, 14, 2])
# a2 = Alternative("a2", [2170, 13.8, 11, 5])
# a3 = Alternative("a3", [2178, 13.2, 11, 3])
# a4 = Alternative("a4", [2290, 17.5, 13, 3])
#
# alternatives = [a1, a2, a3, a4]
#
# dm = DecisionMatrix(criteria, alternatives,
#                     DecisionMatrix.normalize_l2)
# weights = [0.4, 0.3, 0.2, 0.1]
#
# el = Electre(dm, weights)
# el.calculate_electre()