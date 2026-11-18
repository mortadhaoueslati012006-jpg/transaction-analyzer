"""Transaction Analyzer: a small fintech tool that reads bank transactions
from a CSV file, summarizes them, and flags suspicious ones."""

import csv
import sys
from collections import defaultdict


def load_transactions(path):
    """Read the CSV file and return a list of transactions (dicts)."""
    transactions = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions


def summarize(transactions):
    """Compute total income, total expenses, balance and spending per category."""
    income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = -sum(t["amount"] for t in transactions if t["amount"] < 0)
    by_category = defaultdict(float)
    for t in transactions:
        if t["amount"] < 0:
            by_category[t["category"]] += -t["amount"]
    return income, expenses, income - expenses, by_category


def find_suspicious(transactions, factor=5):
    """Flag two kinds of transactions:
    1. Unusually large expenses (more than `factor` times the average expense).
    2. Possible duplicates (same date, description and amount).
    """
    expenses = [t for t in transactions if t["amount"] < 0]
    average = sum(-t["amount"] for t in expenses) / len(expenses)
    flagged = []
    seen = set()
    for t in expenses:
        key = (t["date"], t["description"], t["amount"])
        if -t["amount"] > factor * average:
            flagged.append((t, "unusually large amount"))
        if key in seen:
            flagged.append((t, "possible duplicate"))
        seen.add(key)
    return flagged


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "transactions.csv"
    transactions = load_transactions(path)
    income, expenses, balance, by_category = summarize(transactions)

    print("=== Summary ===")
    print(f"Income:   {income:10.2f}")
    print(f"Expenses: {expenses:10.2f}")
    print(f"Balance:  {balance:10.2f}")

    print("\n=== Spending by category ===")
    for category, total in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"{category:<12}{total:10.2f}  ({total / expenses:.0%})")

    print("\n=== Suspicious transactions ===")
    flagged = find_suspicious(transactions)
    if not flagged:
        print("None found.")
    for t, reason in flagged:
        print(f"{t['date']}  {t['description']:<15}{t['amount']:10.2f}  -> {reason}")


if __name__ == "__main__":
    main()
