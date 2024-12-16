from backend.mcda.core.core import Criterion, Alternative
from backend.mcda.core.core import DecisionMatrix, Pairwise
from backend.mcda.methods.ahp import AHP
from backend.mcda.methods.electre import Electre
from backend.mcda.methods.promethee import Promethee
from backend.mcda.methods.smart import SMART
from backend.mcda.methods.topsis import Topsis
from backend.mcda.methods.weightedSum import WeightedSum


def input_criteria():
    print("Please enter criteria below.")

    criteria = []
    while (True):
        name = input("Criteria name: ")

        beneficiality = None
        while (beneficiality != "max" and beneficiality != "min"):
            beneficiality = input(
                "Is this criteria beneficial or non-beneficial (Please enter max for 'beneficial' and min for 'non-beneficial'): ")

            if beneficiality != "max" and beneficiality != "min":
                print("Please enter only min or max")

        criterion = Criterion(name=name, min_max=beneficiality)
        criteria.append(criterion)

        continue_flag = input(
            "Would you like to add more criteria? Please press 1 to continue or anything else to stop: ")
        if continue_flag != "1":
            return criteria


def input_alternatives(criteria):
    print("Please enter alternatives below.")

    alternatives = []
    while (True):
        name = input("Alternative name: ")

        values = []
        for i in range(len(criteria)):
            print("Please enter value for", criteria[i].name)
            val = input("Value: ").replace(" ", "")
            # categorical data will raise some errors when casted to float!
            values.append(float(val))

        alternatives.append(Alternative(name=name, values=values))

        continue_flag = input(
            "Would you like to add more alternatives? Please press 1 to continue or anything else to stop: ")
        if continue_flag != "1":
            return alternatives

def input_weights(criteria):
    print("\nWeights will now be calculated using the pairwise method. \nThe following scale can be used to determine the relative importance of one criteria to another.\n")
    print("+---------+------------------------+---------------------------------------------------------------------------------------+")
    print("|  Value  |       Definition       |                            Description                                                |")
    print("+---------+------------------------+---------------------------------------------------------------------------------------+")
    print("|      -8 | Absolute Importance    | First criteria is of the least importance; Not subject of any doubt                    |")
    print("|      -6 | Significant Importance | First criteria is significantly less important                                        |")
    print("|      -4 | Substantial Importance | First criteria is substantially less important                                        |")
    print("|      -2 | Low Importance         | First criteria is slightly less important                                             |")
    print("|       0 | Equal Importance       | Both criteria have equal importance                                                   |")
    print("|       2 | Low Importance         | First criteria is slightly more important                                             |")
    print("|       4 | Substantial Importance | First criteria is substantially more important                                        |")
    print("|       6 | Significant Importance | First criteria is significantly more important                                        |")
    print("|       8 | Absolute Importance    | First criteria is of the most importance; Not subject of any doubt                    |")
    print("| 1,3,5,7 | Intermediate values    | Necessary intermediate values                                                         |")
    print("+---------+------------------------+---------------------------------------------------------------------------------------+")

    values = []
    for row in range(len(criteria)):
        for col in range(row + 1, len(criteria)):
            if row == col:
                continue
            else:
                print("How important is", criteria[row].name, "with respect to", criteria[col].name)
                user_input = float(input("Enter: "))
                if user_input < 0:
                    user_input *= -1
                    user_input += 1
                    user_input = 1 / user_input
                else:
                    user_input += 1

                values.append(user_input)

    pairwise = Pairwise(values)
    return pairwise.calculate_eigenvector()

def main_menu():
    print("\n===== PROGRAM STARTED =====\n")

    criteria = input_criteria()
    alternatives = input_alternatives(criteria)
    weights = input_weights(criteria)
    decision_matrix = DecisionMatrix(criteria, alternatives, DecisionMatrix.normalize_l2)

    while (True):
        print(
            "\nPlease choose which method to use:\n[1] AHP \n[2] Electre \n[3] Promethee \n[4] SMART \n[5] TOPSIS \n[6] Weighted Sum Method")

        method = None
        result = None
        chosen_method = input("\nPlease select a method: ")

        if chosen_method == "1":
            method = AHP(decision_matrix, weights)
            result = method.calculate_ahp()
            continue
        elif chosen_method == "2":
            method = Electre(decision_matrix, weights)
            result = method.calculate_electre()
        elif chosen_method == "3":
            method = Promethee(decision_matrix, weights)
            result = method.calculate_promethee()
        elif chosen_method == "4":
            method = SMART(decision_matrix, weights)
            result = method.calculate_smart()
        elif chosen_method == "5":
            method = Topsis(decision_matrix, weights)
            result = method.calculate_topsis()
        elif chosen_method == "6":
            method = WeightedSum(decision_matrix, weights)
            result = method.calculate_weighted_sum()
        else:
            print("\nError! Choose again...")
            continue

        if result != None:
            print(result)

        continue_flag = input(
            "\nWould you like to calculate again with a different method? Please press 1 to continue or anything else to stop: ")
        if continue_flag != "1":
            break

    print("\n===== PROGRAM END =====\n")
