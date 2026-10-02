# create a backend for CDM Machine
#need to be a menu driven system ( check balance, withdraw, deposit)

# save a PIN CARD number and check your user input pin number
# money can be withdraw and deposit
#when depositing you get 10% cashback
#when withdraw every rs.5 deduct from the account


PIN = "0000"
ACCOUNT_BALANCE = 20000


pin = input("Enter your PIN Number : ")

if pin == PIN :
    menu = input("1. Check Balance"
                 "\n2.Withdraw"
                 "\n3.Deposit"
                 "\nSelect Menu Number")

    if menu == "1":
        print(f"Your Account Balance is {ACCOUNT_BALANCE}.")

    if menu == "2":
        withdraw_amount = float(input("Enter Withdraw Amount"))

        if withdraw_amount + 5 < ACCOUNT_BALANCE :
            print("Please Take Your Money.")
            print(f"Your New balance is {ACCOUNT_BALANCE - withdraw_amount -5 }")
        else:
            print("Insufficient Amount.")
    
else:
    print("Invalid PIN number. Try Again")


