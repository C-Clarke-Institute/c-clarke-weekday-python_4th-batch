from typing import List

from day_14.sampath.account import Account
from day_14.sampath.users import User


class CurrentAccount(Account):
    def __init__(self, account_no : str, branch : str, balance: float, user: User, cheque_ids : List[str]):
        super().__init__(account_no=account_no, branch=branch, balance=balance, user=user)
        self.__cheque_ids = cheque_ids

    def get_cheque_ids(self):
        return self.__cheque_ids

    def add_cheque_id(self, cheque_id : str) -> None:
        self.__cheque_ids.append(cheque_id)

if __name__ == '__main__':

    curr_accnt = CurrentAccount("23232323",
                                "moratuwa"
                                , 2332323.23
                                , "sdsdsd", ["232323", "23232323"])
    curr_accnt.show_account_details()