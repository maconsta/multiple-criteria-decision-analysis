from methods.electre import Electre
from methods.promethee import Promethee
from methods.smart import SMART
from methods.topsis import Topsis
from methods.weightedSum import WeightedSum
from core.core import DecisionMatrix, Pairwise
from input_handlers import input_criteria, input_alternatives

if __name__ == "__main__":
    print("\n===== PROGRAM STARTED =====\n")

    criteria = input_criteria()
    alternaties = input_alternatives(criteria)

    decision_matrix = DecisionMatrix(criteria, alternaties)

    print("\nWeights will now be calculated using the pairwise method. \nThe following scale can be used to determine the relative importance of one criteria to another.\n")
    print("+---------+------------------------+-------------------------------------------------------------------+")
    print("|  Value  |       Definition       |                            Description                            |")
    print("+---------+------------------------+-------------------------------------------------------------------+")
    print("|       1 | Equal Importance       | Both criteria have equal importance                               |")
    print("|       3 | Low Importance         | One criteria is slightly more important                           |")
    print("|       5 | Substantial Importance | One criteria is substantially more important                      |")
    print("|       7 | Significant Importance | One criteria is significantly more important                      |")
    print("|       9 | Absolute Importance    | This criteria is of the most importance; Not subject of any doubt |")
    print("| 2,4,6,8 | Intermediate values    | Necessary intermediate values                                     |")
    print("+---------+------------------------+-------------------------------------------------------------------+")

    pairwise = Pairwise(criteria)
    pairwise.fill_matrix()
    weights = pairwise.calculate_eigenvector()

    while (True):
        print("\nPlease choose which method to use:\n[1] AHP (under construction) \n[2] Electre \n[3] Promethee \n[4] SMART \n[5] TOPSIS \n[6] Weighted Sum Method")

        method = None
        result = None
        chosen_method = input("\nPlease select a method: ")

        match chosen_method:
            case "1":
                print("\nNot active at the moment, please choose another method.")
                continue
            case "2":
                method = Electre(decision_matrix, weights)
                result = method.calculate_electre()
            case "3":
                method = Promethee(decision_matrix, weights)
                result = method.calculate_promethee()
            case "4":
                method = SMART(decision_matrix, weights)
                result = method.calculate_smart()
            case "5":
                method = Topsis(decision_matrix, weights)
                result = method.calculate_topsis()
            case "6":
                method = WeightedSum(decision_matrix, weights)
                result = method.calculate_weighted_sum()
            case _:
                print("\nError! Choose again...")
                continue
        
        if result != None:
            print(result)

        continue_flag = input(
            "\nWould you like to calculate again with a different method? Please press 1 to continue or anything else to stop: ")
        if continue_flag != "1":
            break

    print("\n===== PROGRAM END =====\n")
