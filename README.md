# Budget

This project contains a Python implementation of a simple budget app that allows users to track their spending across different categories. It features a `Category` class to represent budget categories like food, clothing, and entertainment, and includes functionalities to deposit, withdraw, transfer funds between categories, and check balances. Additionally, it provides a utility function to visualize spending by category as a bar chart.

## Features

- **Category Management**: Create categories for budgeting.
- **Transactions**: Record deposits and withdrawals within categories.
- **Fund Transfers**: Transfer funds between budget categories.
- **Balance Checking**: Check the current balance of any budget category.
- **Spending Visualization**: Visualize spending across categories with a bar chart.

## Usage

### Setting Up Categories

To start using the budget app, first instantiate objects of the `Category` class:

```python
from budget_app import Category

food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")
```

### Managing Transactions

You can add deposits and withdrawals for each category:

```python
food.deposit(1000, "Initial deposit")
food.withdraw(100, "Groceries")
clothing.deposit(500, "Clothes fund")
```

### Transferring Funds

Transferring funds between categories is straightforward:

```python
food.transfer(50, clothing)
```

### Checking Balances

To check the balance of any category:

```python
print(food.get_balance())
```
