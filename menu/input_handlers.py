from core.core import Criterion, Alternative
from core.core import DecisionMatrix, Pairwise
from methods.ahp import AHP
from methods.electre import Electre
from methods.promethee import Promethee
from methods.smart import SMART
from methods.topsis import Topsis
from methods.weightedSum import WeightedSum


def input_criteria():
    print("Please enter criteria below.")

    criteria = []
    while (True):
        name = input("Criteria name: ")

        beneficiality = None
        while (beneficiality != "1" and beneficiality != "2"):
            beneficiality = input(
                "Is this criteria beneficial or non-beneficial (Please enter 1 for 'beneficial' and 2 for 'non-beneficial'): ")

            if beneficiality != "1" and beneficiality != "2":
                print("Please enter only 1 or 2")

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
            val = input("Value: ")
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
    print("|       0 | Skip Comparison        | Use this when the second criteria is more important; The program will ask again later |")
    print("|       1 | Equal Importance       | Both criteria have equal importance                                                   |")
    print("|       3 | Low Importance         | First criteria is slightly more important                                             |")
    print("|       5 | Substantial Importance | First criteria is substantially more important                                        |")
    print("|       7 | Significant Importance | First criteria is significantly more important                                        |")
    print("|       9 | Absolute Importance    | First criteria is of the most importance; Not subject of any doubt                    |")
    print("| 2,4,6,8 | Intermediate values    | Necessary intermediate values                                                         |")
    print("+---------+------------------------+---------------------------------------------------------------------------------------+")

    pairwise = Pairwise(criteria)
    pairwise.fill_matrix()
    return pairwise.calculate_eigenvector()

def main_menu():
    print("\n===== PROGRAM STARTED =====\n")

    criteria = input_criteria()
    alternaties = input_alternatives(criteria)
    weights = input_weights(criteria)
    decision_matrix = DecisionMatrix(criteria, alternaties)

    while (True):
        print(
            "\nPlease choose which method to use:\n[1] AHP \n[2] Electre \n[3] Promethee \n[4] SMART \n[5] TOPSIS \n[6] Weighted Sum Method")

        method = None
        result = None
        chosen_method = input("\nPlease select a method: ")

        if chosen_method == "1":
            # method = AHP(decision_matrix, weights)
            # result = method.calculate_ahp()
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
