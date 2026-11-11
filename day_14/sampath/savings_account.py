from day_14.sampath.account import Account


class SavingsAccount(Account):
    def __init__(self, account_no, branch, balance, user, atm_card_no):
        super().__init__(account_no=account_no, branch=branch, balance=balance, user=user)
        self.__atm_card_no = atm_card_no


    def get_atm_card_no(self):
        return self.__atm_card_no

    def set_atm_card_no(self, card_no):
        self.__atm_card_no = card_no


