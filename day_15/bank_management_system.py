#Objectives - develop a bank managemeent system using pyton oop concepts including
# classes, objects, constructions, inheritance, method overriding, and polymorphism




# - Create a Basic Bank Account with account holder and balance
# - implement a suitable constructor
# - create a method to display account holder's name and acccount balance
# - Add methods to deposit cash & withdraw
#           - with suitable validations
#           - Display appropriate success or error messages
#           - prevent negative or zero transactions

# ------------
# create savings account that inherits from Bank Account class
# - implement a proper constructor with account holder, balance and
# interest rate (default = 5%)
# - implement a  add interest method to calculate interest and update the balance

# ------------
# create Current account that inherits from Bank Account class
# - implement a proper constructor with acccount holder, balance and
# overdraft limit (default = 20000)
# -override the withdraw method to allow upto balance + overdraft limit


# -------
# implement account selection andd banking menu
# - create account - ask the user to enter name and intial amount
# - allow them to choose between current and savings
#  - create appropriate account object
# implement menu and call suitable methods

# --- Bank Menu --
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Add interest
# 5. Exit

#handle invalid inputs and continue display menu until user choose to exit

# use isinstance()


