from bankaccount import BankAccount, Result

makeOperations = True

print("Welcome to Jbank!")
account = BankAccount()

while(makeOperations == True):
    decision = int(input('''What do you want to do?
    1 - Show account status
    2 - Deposit cash
    3 - Withdraw cash
    4 - Quit
    -> '''))
    if(decision == 1):
        print("\nCurrent cash amount on your account is:", account)

    elif(decision == 2):
        account.deposit(
            int(input("\nHow much cash do you want to deposit?->")))

    elif(decision == 3):
        result = account.tryWithdraw(
            int(input("\nHow much cash do you want to withdraw?->")))
        print(result.message, result.value)

    elif(decision == 4):
        makeOperations = False

    else:
        print("\nChoose the correct number!")

    print()
