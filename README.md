# Transaction Analyzer

A small Python tool that reads bank transactions from a CSV file, summarizes income and spending, and flags suspicious transactions. Built as a beginner-friendly fintech project.

## Features
- Total income, expenses and balance
- Spending breakdown by category (with percentages)
- Basic fraud detection rules:
  - unusually large expenses (more than 5x the average expense)
  - possible duplicate transactions (same date, description and amount)

## Technologies
Python 3 (standard library only: `csv`, `collections`)

## How to run
```
git clone https://github.com/YOUR_USERNAME/transaction-analyzer.git
cd transaction-analyzer
python main.py
```
To analyze your own file: `python main.py my_transactions.csv`

The CSV must have these columns: `date,description,category,amount` (expenses are negative).

## Example output
```
=== Summary ===
Income:      2900.00
Expenses:    2308.50
Balance:      591.50

=== Spending by category ===
Shopping       1200.00  (52%)
Housing         800.00  (35%)
...

=== Suspicious transactions ===
2026-10-08  Online store     -1200.00  -> unusually large amount
2026-10-09  Coffee              -4.50  -> possible duplicate
```

## Ideas for improvement
- Add charts with matplotlib
- Export the report to PDF or Excel
- Store transactions in an Oracle or SQLite database
- Add more fraud rules (unusual hours, new merchants)

## Author
Mortadha Oueslati
