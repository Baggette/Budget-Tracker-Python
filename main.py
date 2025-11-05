import json

try:
    f = open("./data.json", "r")
except FileNotFoundError:
    f = open("./data.json", "w")

f = open("./data.json", "r")

budgetData = json.load(f)
mainMenuMSG = """\nPersonal Budget Tracker
1. Income and Expense Tracking
2. Budget management 
3. View all transactions
4. Save and Exit

Select an option: """
#this is a change
   
addIncomeMSG = """Budget Management 
1. Add income
2. Add expense 
3. Exit

Select an option: """

def addIncome():
    option = input(addIncomeMSG)
    if option == "1":
        description = input("Income Description: ")
        try:
            amount = float(input("Monthly income: "))
            budgetData["income"].append({"description" : description, "income_amount" : amount})
            print(budgetData)
        except ValueError:  
            input("You did not enter a valid number! \nPress enter to continue")
            addIncome()


while True:
    option = input(mainMenuMSG).strip()
    if option == "1":
        addIncome()
        continue
    elif option == "4":
        saveAndExit()
    

    