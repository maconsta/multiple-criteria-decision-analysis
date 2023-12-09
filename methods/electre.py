import numpy as np
from core.core import Criterion, Alternative, DecisionMatrix


class Electre:
    def __init__(self, decision_matrix:  DecisionMatrix, weights: list):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.concordance_interval_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.concordance_index_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.discordance_interval_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.discordance_index_matrix = np.zeros((self.decision_matrix.alt_count, self.decision_matrix.alt_count))
        self.net_superior_vector = np.zeros(self.decision_matrix.alt_count)
        self.net_inferior_vector = np.zeros(self.decision_matrix.alt_count)

    def weigh(self):  # DOESNT WORK PROPERLY?????
        for col in range(self.decision_matrix.normalized_matrix.shape[0]):
            self.decision_matrix.normalized_matrix[:, col] *= self.weights[col]

    def calculate_concordance_interval_matrix(self):
        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if i == j:
                    continue

                for k in range(self.decision_matrix.crit_count):
                    if self.decision_matrix.normalized_matrix[i][k] >= self.decision_matrix.normalized_matrix[j][k]: # трябва ли да е по-голями и равно или само по-голямо като проверяваме за доминантност
                        self.concordance_interval_matrix[i][j] += self.weights[k]

    def calculate_concordance_index_matrix(self):
        col_sums = np.sum(self.concordance_interval_matrix, axis=0)
        c_threshold = np.sum(col_sums) / (
            self.decision_matrix.alt_count * (self.decision_matrix.alt_count - 1))

        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
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
                    abs_vector.append(abs(self.decision_matrix.normalized_matrix[i][k] - self.decision_matrix.normalized_matrix[j][k]))

                    if self.decision_matrix.normalized_matrix[i][k] < self.decision_matrix.normalized_matrix[j][k]:
                        discordance_abs_vector.append(abs(self.decision_matrix.normalized_matrix[i][k] - self.decision_matrix.normalized_matrix[j][k])) 
                
                for k in range(self.decision_matrix.crit_count):
                    if self.decision_matrix.normalized_matrix[i][k] < self.decision_matrix.normalized_matrix[j][k]: # трябва ли да е по-голями и равно или само по-голямо като проверяваме за доминантност
                        self.discordance_interval_matrix[i][j] = max(discordance_abs_vector)/max(abs_vector)

    def calculate_discordance_index_matrix(self):
        col_sums = np.sum(self.discordance_interval_matrix, axis=0)
        d_threshold = np.sum(col_sums) / (
            self.decision_matrix.alt_count * (self.decision_matrix.alt_count - 1))
        
        # print(d_threshold)

        for i in range(self.decision_matrix.alt_count):
            for j in range(self.decision_matrix.alt_count):
                if self.discordance_interval_matrix[i][j] <= d_threshold:
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

    def calculate_electre(self):
        self.decision_matrix.normalize_l2()
        # print("\nNormalized DM")
        # print(self.decision_matrix.normalized_matrix)

        self.decision_matrix.normalized_matrix *= self.weights
        # print("\nNormalized Weighted DM")
        # print(self.decision_matrix.normalized_matrix)

        self.calculate_concordance_interval_matrix()
        # print("\nConcordance Interval Matrix")
        # print(self.concordance_interval_matrix)

        self.calculate_concordance_index_matrix()
        # print("\nConcordance Index Matrix")
        # print(self.concordance_index_matrix)

        self.calculate_discordance_interval_matrix()
        # print("\nDiscordance Interval Matrix")
        # print(self.discordance_interval_matrix)

        self.calculate_discordance_index_matrix()
        # print("\nDiscordance Index Matrix")
        # print(self.discordance_index_matrix)

        self.calculate_net_superior_vector()
        # print("\nNet Superior Vector")
        # print(self.net_superior_vector)

        self.calculate_net_inferior_vector()
        # print("\nNet Inferior Vector")
        # print(self.net_inferior_vector)

        # по кой вектор ранкираме резултата? 
        # >= или > при сравненията за доминантност? 
        # трябва ли да се направи агрегирана матрица?

        result = []
        for i in range(len(self.net_superior_vector)):
            name = self.decision_matrix.alternatives[i].name
            result.append({"name": name, "score": self.net_superior_vector[i]})

        result = sorted(result, key=lambda d: d['score'], reverse=True)

        return result



# c1 = Criterion("c1", "max")
# c2 = Criterion("c2", "max")
# c3 = Criterion("c3", "max")
# c4 = Criterion("c4", "max")
# c5 = Criterion("c5", "max")
# c6 = Criterion("c6", "max")
# criteria = [c1, c2, c3, c4, c5, c6]

# a1 = Alternative("a1", [1350, 1850, 7.5, 2.58, 93.5, 0.045])
# a2 = Alternative("a2", [1680, 1650, 8.5, 3.75, 95.3, 0.068])
# a3 = Alternative("a3", [1560, 1950, 6.5, 4.86, 88.6, 0.095])
# a4 = Alternative("a4", [1470, 1850, 9.5, 3.16, 98.4, 0.072])
# alternatives = [a1, a2, a3, a4]

# dm = DecisionMatrix(criteria, alternatives)
# weights = [0.2336, 0.1652, 0.3355, 0.1021, 0.0424, 0.1212]

# el = Electre(dm, weights)
# print(el.calculate_electre())
