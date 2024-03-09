class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_balance = 0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items_str = ""
        for item in self.ledger:
            items_str += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total_str = f"Total: {self.get_balance():.2f}"
        return title + items_str + total_str


def create_spend_chart(categories):
    total_spent = sum(
        sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    )
    category_spends = [
        (
            category.name,
            sum(-item["amount"] for item in category.ledger if item["amount"] < 0),
        )
        for category in categories
    ]

    percentages = [
        (name, (spent / total_spent) * 100) for name, spent in category_spends
    ]

    chart = "Percentage spent by category\n"
    for percentage in range(100, -10, -10):
        chart += f"{percentage:>3}| "
        for _, spent in percentages:
            chart += "o  " if spent >= percentage else "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n     "

    max_length_name = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_length_name) for category in categories]
    for x in zip(*names):
        chart += "  ".join(x) + "  \n     "

    return chart.rstrip() + "  "
