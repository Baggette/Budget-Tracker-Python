import json

try:
    f = open("./data.json", "r")
except FileNotFoundError:
    f = open("./data.json", "w")

f = open("./data.json", "r")

budgetData = json.load(f)
mainMenuMSG = """\nPersonal Budget Tracker\n
1. Income and Expense Tracking
2. Budget management 
3. View all transactions
4. Save and Exit

Select an option: """
#this is a change
   
addIncomeMSG = """\nBudget Management\n
1. Add income
2. Add expense 
3. Exit

Select an option: """

expenseCategoryMSG = """\nExpense Category\n
1. Food
2. Transportation
3. Entertainment
4. Bills
5. Other

Select an option: """

categories = ["food","transportation", "Entertainment", "bills", "other"]
def addIncome():
    option = input(addIncomeMSG).strip()
    if option == "1":
        description = input("Income Description: ")
        try:
            amount = float(input("Monthly income: "))
            budgetData["income"].append({"description" : description, "income_amount" : amount})
            print(budgetData)
        except ValueError:  
            input("You did not enter a valid number! \nPress enter to continue...")
            addIncome()
    elif option == "2":
        try:
            category = int(input(expenseCategoryMSG))
            if category <= 0 or category > 5:
                raise ValueError
            else:
                description = input("Expense Description: ")
                amount = float(input(""))
        except ValueError:
            input("You did not enter a valid number!\nPress enter to continue...")
            addIncome()


while True:
    option = input(mainMenuMSG).strip()
    if option == "1":
        addIncome()
        continue
    elif option == "4":
        saveAndExit()
    

    