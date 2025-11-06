import json
from datetime import datetime

# ----------- Transaction Class -----------
class Transaction:
    """Class to represent a financial transaction with description, amount, category and type"""
    def __init__(self, description, amount, category=None, t_type=None):
        """Initialize a new transaction with given parameters"""
        self.description = description
        self.amount = amount
        self.category = category
        self.t_type = t_type
        self.timestamp = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert transaction to dictionary format for JSON storage"""
        data = {
            "description": self.description,
            "timestamp": self.timestamp
        }
        # Add amount based on transaction type
        if self.t_type == "income":
            data["income_amount"] = self.amount
        elif self.t_type == "expense":
            data["expense_amount"] = self.amount
        return data

# ----------- File Setup -----------
# Check if data file exists, if not create it with initial structure
try:
    f = open("./data.json", "r")
    f.close()
except FileNotFoundError:
    f = open("./data.json", "w")
    # Initialize empty data structure with income array and expense categories
    f.write(json.dumps({"income": [], "expense": [{"food": [], "transportation": [], "entertainment": [], "bills": [], "other": []}]}))
    f.close()

# Load existing budget data
f = open("./data.json", "r")
budgetData = json.load(f)
f.close()

# Define menu messages for different operations
mainMenuMSG = """\nPersonal Budget Tracker\n
1. Income and Expense Tracking
2. Budget management 
3. View all transactions
4. Save and Exit

Select an option: """

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

# List of valid expense categories
categories = ["food", "transportation", "entertainment", "bills", "other"]

# ----------- Add Income / Expense -----------
def addIncome():
    """Handle adding new income or expense transactions"""
    option = input(addIncomeMSG).strip()
    if option == "1":
        # Add new income
        description = input("Income Description: ")
        try:
            amount = float(input("Monthly income: $"))
            transaction = Transaction(description, amount, t_type="income")
            budgetData["income"].append(transaction.to_dict())
            input("Income added successfully!\n\nPress enter to continue...")
        except ValueError:
            input("You did not enter a valid number! \n\nPress enter to continue...")
            addIncome()
    elif option == "2":
        # Add new expense
        try:
            category = int(input(expenseCategoryMSG))
            if category <= 0 or category > 5:
                raise ValueError
            description = input("Expense Description: ")
            amount = float(input("Expense amount: $"))
            transaction = Transaction(description, amount, category=categories[category - 1], t_type="expense")
            budgetData["expense"][0][categories[category - 1]].append(transaction.to_dict())
            input(f"Successfully added \"{description}\" to the {categories[category - 1]} category with an amount of {amount}$ \nPress enter to continue...")
        except ValueError:
            input("You did not enter a valid number!\nPress enter to continue...")
            addIncome()
    elif option == "3":
        return
    else:
        input("Invalid option\nPress enter to continue...")

# ----------- Budget Management Setup -----------
if "budget" not in budgetData:
    budgetData["budget"] = {cat: 0.0 for cat in categories}

def getCategorySpending(category_name):
    """Calculate total spending for a given category"""
    total = 0.0
    for record in budgetData["expense"][0][category_name]:
        total += record.get("expense_amount", 0.0)
    return total

def setBudgetLimits():
    """Set monthly budget limits for each category"""
    print("\n=== Set Mothly Budget Limits ===\n")
    for cat in categories:
        while True:
            try:
                amount = float(input(f"Enter monthly budget for {cat.title()}: $"))
                break
            except ValueError:
                print("You did not enter a valid number, please try again.")
        budgetData["budget"][cat] = amount
    input("\nBudgets updated successfully!\nPress enter to continue...")

def showBudgetStatus():
    """Display current budget status for all categories"""
    print("\n=== Budget Status ===\n")
    for cat in categories:
        limit = budgetData["budget"].get(cat, 0.0)
        spent = getCategorySpending(cat)
        remaining = limit - spent

        # Print budget details for each category
        print(f"Category: {cat.title()}")
        print(f"  Budget:    ${limit:.2f}")
        print(f"  Spent:     ${spent:.2f}")
        print(f"  Remaining: ${remaining:.2f}")

        # Show percentage used and warnings if approaching/exceeding budget
        if limit > 0:
            used_percent = (spent / limit) * 100
            print(f"  Used:   {used_percent:.0f}%")
            if used_percent >= 100:
                print("  WARNING: You are over budget in this category!")
            elif used_percent >= 80:
                print("  WARNING: You have used more than 80% of this budget")
        else:
            print("  No budget set for this category.")
        print()
    input("Press enter to continue...")

budgetMenuMSG = """\nBudget Management\n
1. Set monthly budget limits
2. View budget status
3. Back to main menu

Select an option: """

def budgetManagement():
    """Handle budget management operations"""
    while True:
        choice = input(budgetMenuMSG).strip()
        if choice == "1":
            setBudgetLimits()
        elif choice == "2":
            showBudgetStatus()
        elif choice == "3":
            return
        else:
            input("Invalid option\nPress enter to continue...")

# ----------- Report -----------
def generateReport():
    """Generate and display summary report of all transactions"""
    totalIncome = 0
    totalExpense = 0
    category = {"food": 0, "transportation": 0, "entertainment": 0, "bills": 0, "other": 0}
    
    # Calculate total income
    for item in budgetData.get("income", []):
        try:
            totalIncome += float(item.get("income_amount", 0.0))
        except (TypeError, ValueError):
            continue

    # Calculate total expenses by category
    for cat in budgetData.get("expense", [{}])[0].keys():
        for item in budgetData["expense"][0].get(cat, []):
            amt = float(item.get("expense_amount", 0.0))
            totalExpense += amt
            category[cat] += amt

    # Display report
    print("\n=== Transaction Summary ===\n")
    print(f"Total Income:  ${totalIncome:.2f}")
    print(f"Total Expense: ${totalExpense:.2f}")
    print(f"Remaining:     ${totalIncome - totalExpense:.2f}")
    print("\nCategory Breakdown:")
    for k, v in category.items():
        print(f"  {k.title()}: ${v:.2f}")
    input("\nPress enter to continue...")

# ----------- Save and Exit -----------
def saveAndExit():
    """Save current data to file and exit program"""
    with open("./data.json", "w") as f:
        json.dump(budgetData, f, indent=4)
    print("\nData saved successfully. Exiting...")
    exit()

# ----------- Main Loop -----------
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
