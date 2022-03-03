class BankAccount:

    def __init__(self, balance=0):

        self.balance = balance

    def deposit(self, cashAmount):
        "Valid the cash"

        self.balance += cashAmount

    def tryWithdraw(self, cashAmount):

        if(self.balance >= cashAmount):

            self.balance -= cashAmount

            return Result(True, "Cash withdrawn:", cashAmount)

        else:
            return Result(False, "Cash withdrawal failed: Not enough cash, you got only:", self.balance)

    def __str__(self):

        return str(self.balance)


class Result:
    def __init__(self, isSuccess, message, value=None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value
