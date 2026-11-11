from day_14.sampath.users import User


class Account:

    def __init__(self, account_no: str, branch: str, balance: float, user: User): #constructor
        self.__account_no = account_no #instance variable
        self.__branch = branch
        self.__balance = balance
        self.__user = user #has a relationship/ composition

    def show_account_details(self) -> None:
        print(f"Account no - {self.__account_no} | branch - {self.__branch} | Balance - {self.__balance}")

    def deposit(self, amount) -> str:
        if amount < 0:
            return "Invalid amount"
        self.__balance += amount
        return "Successfully updated the balance"

    def withdraw(self, withdraw_amount) -> str:
        if self.__balance < withdraw_amount:
            return "Invalid amount"
        self.__balance -= withdraw_amount
        return "Not enough balance"

    def get_account_no(self) -> str:
        return self.__account_no

    def get_balance(self) -> float:
        return self.__balance

    def set_user(self, user) -> None:
        self.__user = user

    def get_user(self) -> User:
        return self.__user

    def check_balance(self):
        print(f"{self.__account_no} balance is - {self.__balance}")

    def __str__(self): #Overriding the object class __str__ method
        return self.__account_no

if __name__ == '__main__':

    user1 = User(nic="2323233V", name="saman", age=12)
    user2 = User(nic="2323233V", name="saman", age=12)
    accnt1 = Account(account_no="293203", branch="moratuwa", balance=2323233.0, user=user1)
    accnt2 = Account(account_no="293203", branch="moratuwa", balance=2323233.0, user=user2)

    print(accnt1.get_user().get_name())

    accnt1.deposit(344343)

    accnt1.show_account_details()
    print(accnt1)

