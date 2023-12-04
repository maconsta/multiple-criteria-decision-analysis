from core.core import Criterion, Alternative

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
            values.append(int(val)) # categorical data will raise some errors when casted to int!
        
        alternatives.append(Alternative(name=name, values=values))

        continue_flag = input(
            "Would you like to add more alternatives? Please press 1 to continue or anything else to stop: ")
        if continue_flag != "1":
            return alternatives