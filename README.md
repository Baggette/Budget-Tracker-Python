# Budget Tracker

A command-line personal budget tracking application built with Python that helps users manage their finances by tracking income, expenses, and budget limits.

## Features

- Income and expense tracking with transaction history
- Category-based expense management with budget limits
- Monthly financial reporting
- Summary report generation
- Real-time budget monitoring with warnings
- Persistent data storage using JSON

### Expense Categories
- Food
- Transportation
- Entertainment
- Bills
- Other

## Prerequisites

- Python 3.x
- No additional packages required (uses only built-in Python modules)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Baggette/Budget-Tracker-Python.git
```

2. Navigate to the project directory:
```bash
cd Budget-Tracker-Python
```

## Usage

Run the program using Python:
```bash
python main.py
```

### Main Menu Options

1. **Income and Expense Tracking**
   - Add new income transactions with descriptions
   - Record expenses with categories and descriptions
   - Automatic timestamp recording for all transactions

2. **Budget Management**
   - Set monthly budget limits for each category
   - View detailed budget status for all categories
   - Get warnings at 80% and 100% budget utilization
   - View remaining budget amounts

3. **View All Transactions**
   - See transaction summaries
   - View total income and expenses
   - Check category-wise expense breakdown
   - Calculate remaining balance

4. **Generate Monthly Report**
   - Comprehensive financial analysis
   - Savings rate calculation
   - Top spending categories
   - Budget utilization statistics
   - Categories exceeding 80% usage

5. **Save and Exit**
   - Automatically saves all data to `data.json`
   - Safely exits the program

## Data Structure

The application stores data in `data.json` with the following structure:
```json
{
    "income": [],
    "expense": [
        {
            "food": [],
            "transportation": [],
            "entertainment": [],
            "bills": [],
            "other": []
        }
    ],
    "budget": {
        "food": 0.0,
        "transportation": 0.0,
        "entertainment": 0.0,
        "bills": 0.0,
        "other": 0.0
    }
}
```

## Project Structure

```
Budget-Tracker-Python/
├── main.py          # Main application file with all functionality
├── data.json        # Data storage file (auto-generated)
└── README.md        # Documentation
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Support

If you encounter any problems or have suggestions, please open an issue in the repository.