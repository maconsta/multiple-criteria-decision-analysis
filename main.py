from methods.weightedSum import WeightedSum
from methods.topsis import Topsis
from methods.topsisPairwise import TopsisPairwise
from core.core import Criterion, Alternative, DecisionMatrix

if __name__ == "__main__":

# weighted sum method

# price = Criterion("price", "int", "min")
# mpg = Criterion("mpg", "int", "max")
# hp = Criterion("hp", "int", "max")  
# room = Criterion("room", "int", "max")
# type = Criterion("type", "str", "min")
# age = Criterion("age", "int", "min")
# criteria = [price, mpg, hp, room, type, age]

# # type: 1-Sedan; 2-SUV; 3-Coupe; 4-Truck; 5-Sports
# A1 = Alternative("A1", criteria, [1599, 28, 350, 2, 2, 7])
# A2 = Alternative("A2", criteria, [1899, 16, 200, 4, 1, 3])
# A3 = Alternative("A3", criteria, [1780, 20, 300, 4, 3, 5])
# A4 = Alternative("A4", criteria, [1049, 16.5, 416, 2, 4, 2])
# A5 = Alternative("A5", criteria, [1399, 22, 275, 4, 5, 8])
# alternatives = [A1, A2, A3, A4, A5]

# dm = DecisionMatrix(criteria, alternatives)

# weights = [0.166, 0.166, 0.166, 0.166, 0.166, 0.166]

# ws = WeightedSum(dm, weights)
# result, best_alternative, best_alternative_index = ws.calculate_weighted_sum()
# print("======= WSM =======")
# print(result)
# print("Best Alternative: ", best_alternative_index + 1)



# topsis example
#c1 = Criterion("c1","","max")
#c2 = Criterion("c2","","max")
#c3 = Criterion("c3","","max")
#c4 = Criterion("c4","","max")
#criteria2 = [c1,c2,c3,c4]

#a1 = Alternative("a1",criteria2, [0.751, 0.480, 0.077, 0.066])
#a2 = Alternative("a2",criteria2, [0.178, 0.406, 0.231, 0.615])
#a3 = Alternative("a3",criteria2, [0.071, 0.114, 0.692, 0.319])
#alternatives2 = [a1,a2,a3]

#w = [0.232, 0.402, 0.061, 0.305]
#decisionmatrix = DecisionMatrix(criteria2, alternatives2)
#topsis = Topsis(decisionmatrix, w)
#result, best_alternative, best_alternative_index = topsis.calculate_topsis()
#print("======= Topsis =======")
#print(result)
#print("Best Alternative: ", best_alternative_index + 1)


# topsisPairwise example
 c1 = Criterion("c1","", "max")
 c2 = Criterion("c2","", "max")
 c3 = Criterion("c3","", "max")
 c4 = Criterion("c4","", "max")
 criteria2 = [c1,c2,c3,c4]

 a1 = Alternative("a1", criteria2, [0.751, 0.480, 0.077, 0.066])
 a2 = Alternative("a2", criteria2, [0.178, 0.406, 0.231, 0.615])
 a3 = Alternative("a3", criteria2, [0.071, 0.114, 0.692, 0.319])
 alternatives2 = [a1,a2,a3]

 w = [0.232, 0.402, 0.061, 0.305]
 decisionmatrix = DecisionMatrix(criteria2, alternatives2)

 topsisPairwise = TopsisPairwise(decisionmatrix, w)

 result, best_alternative, best_alternative_index = topsisPairwise.calculate_topsisPairwise()

 print("======= Topsis Pairwise =======")
 print("Scores: ", result)
 print("Best Alternative: ", best_alternative,",", best_alternative_index + 1)