import json
from datetime import datetime
#This is to check if the file exists if not create it 
try:
    f = open("./data.json", "r")
except FileNotFoundError:
    f = open("./data.json", "w")

f = open("./data.json", "r")
#this is a comment
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
#list of categories so I can access the data in the dictonary later
categories = ["food","transportation", "entertainment", "bills", "other"]
def addIncome():
    #get user input
    option = input(addIncomeMSG).strip()
    if option == "1":
        #input for the description field 
        description = input("Income Description: ")
        try:
            amount = float(input("Monthly income: "))
            today = datetime.now().strftime("%Y-%m-%d")
            budgetData["income"].append({"description" : description, "income_amount" : amount, "timestamp" : today})
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
                amount = float(input("Expense amount: "))
                budgetData["expense"][0][categories[category - 1]].append({"description" : description, "expense_amount" : amount})
                input(f"Successfully added \"{description}\" to the {categories[category - 1]} category with an amount of {amount}$ \nPress enter to continue...")
        except ValueError:
            input("You did not enter a valid number!\nPress enter to continue...")
            addIncome()
    elif option == "3":
        return
    else:
        input("Invalid option\nPress enter to continue...")

# Budegt Management

if "budget" not in budgetData:
    budgetData["budget"] = {cat: 0.0 for cat in categories}

#Calculate every category's expense

    def getCategorySpending(category_name): 
        total = 0.0
        for record in budgetData["expense"][0][category_name]:
            total += record.get("expense_amount", 0.0)
            return total

#Setup every month budget for each category
def setBudgetLimits():
    print("\n=== Set Mothly Budget Limits ===\n")
    for cat in categories:
        while True:
            try:
                amount = float(input(f"Enter monthly budget for {cat.title()}: $"))
                break
            except CalueError:
                print("You did not nter a valid number, please try again,")
        budgetData["budget"][cat] = amount
    input("\nBudgets updated successfully!\nPress enter to continue...")

#Check the status of budget: compare income and expense + warning = remaining budget

def showBudgetStatus():
    print("\n=== Budget Status ===\n")
    for cat in categories:
        limit = budgetData["budget"].get(cat, 0.0)
        spent = getCategorySpending(cat)
        remaining = limit - spent

        print(f"Category: {cat.title()}")
        print(f"  Budget:    ${limit:.2f}")
        print(f"  Spent:     ${spent:.2f}")
        print(f"  Remaining: ${remaining:.2f}")

        if limit > 0:
            used_percent + (spent / limit) * 100
            print(f"  Used:   {used_percent:.0f}%")

            #Warning
            if used_percent >= 100:
                print("  WARNING: You are over budget in this category!")
            elif used_percent >= 80:
                print("  WARNING: You have used more than 80% of this budget")
        else:
            print("  No budget set for this category.")
        print()

    input("press enter to continue...")

#Budget Management submenu
budgetMenuMSG = """\nBudget Management\n
1. Set monthly budget limits
2. View budget status
3. Back to main menu

Select an option: """

def budgetManagement():
    while True:
        choice = input(budgetMenuMSG).strip()
        if choice =="1":
            setBudgetLimits()
        elif choice == "2":
            showBudgetStatus()
        elif choice == "3":
            return
        else:
            input("Invalid option\nPress enter to continue...")

def generateReport():
    totalIncome = 0
    totalExpense = 0
    category = {"food" : 0,"transportation" : 0, "entertainment" : 0, "bills" : 0, "other" : 0}
    for item in budgetData["income"]: 
        totalIncome = item["income_amount"] + totalIncome
    print(totalIncome)
    print(budgetData)
    for item in categories:
        try:
            #print(budgetData["expense"][0][item][0]["description"])
            totalExpense = totalExpense + budgetData["expense"][0][item][0]["expense_amount"]
            category[item] = int(budgetData["expense"][0][item][0]["expense_amount"]) + float(category[item])
        except:
            continue
    print(category)
    print(totalExpense)

while True:
    option = input(mainMenuMSG).strip()
    if option == "1":
        addIncome()
        continue
    elif option == "2":
        budgetManagement()
        continue
    elif option == "3":
        generateReport()
    elif option == "4":
        saveAndExit()
    
