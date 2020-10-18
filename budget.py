class Category:
    def __init__(self, catname):

        self.category = catname
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, Category):
        if self.withdraw(amount, "Transfer to " + Category.category):
            Category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def __str__(self):
        stars = "*" * ((30 - len(self.category)) // 2) + self.category
        stars = stars + "*" * (30 - len(stars)) + "\n"

        for item in self.ledger:
            stars += item["description"][:23].ljust(23) + str("{:.2f}".format(
                item["amount"]).rjust(7)) + "\n"

        stars += "Total: " + str(self.balance)
        return stars


def nearest_tenth(num):
    if num < 10:
        return 0
    return round(num / 10.0) * 10


def create_spend_chart(categories):

    withdrwals = []
    c = 0
    length_cat = 0

    for i in categories:

        withdrawn = 0

        for x in i.ledger:

            if x['amount'] < 0:
                withdrawn += -x["amount"]
                c += (-x["amount"])
    if len(i.category) > length_cat:
        length_cat = len(i.category)
    withdrwals.append([i.category, withdrawn])

    for i in withdrwals:
        i.append(nearest_tenth((i[1] / c) * 100))
    c = ""
    c += "Percentage spent by category\n"
    t = 100
    while t >= 0:

        c += str(t).rjust(3) + "|" + " "

        for i in range(len(withdrwals)):
            if withdrwals[i][2] >= t:
                c += "o" + "  "
            else:
                c += "   "
        t -= 10
        c += "\n"

    c += "    " + ("-" * 10) + "\n"

    loop = 0

    for i in range(length_cat):
        c += "     "
        for x in range(len(withdrwals)):
            if len(withdrwals[x][0]) - 1 < loop:
                c += "   "
            else:
                c += withdrwals[x][0][loop] + "  "
        loop += 1
        if i != length_cat - 1:
            c += "\n"
    return c
