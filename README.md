# Budget Tracker

A command-line personal budget tracking application built with Python that helps users manage their finances by tracking income, expenses, and budget limits.

## Features

- Income and expense tracking
- Category-based expense management
- Budget limit setting and monitoring
- Transaction history and reporting
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
   - Add new income transactions
   - Record expenses with categories
   - Each transaction includes description, amount, and timestamp

2. **Budget Management**
   - Set monthly budget limits for each category
   - View current budget status
   - Get warnings when approaching (80%) or exceeding budget limits

3. **View All Transactions**
   - Generate comprehensive financial reports
   - View total income and expenses
   - See category-wise expense breakdown

4. **Save and Exit**
   - Automatically saves all data to `data.json`
   - Safely exits the program

## Data Storage

The application stores all data in a `data.json` file, which:
- Is automatically created on first run
- Maintains transaction history
- Stores budget limits
- Preserves data between sessions

## Project Structure

```
Budget-Tracker-Python/
├── main.py          # Main application file
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