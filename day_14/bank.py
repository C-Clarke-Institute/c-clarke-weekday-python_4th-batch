from typing import List, Optional

from day_14.sampath.current_account import CurrentAccount
from day_14.sampath.savings_account import SavingsAccount
from sampath.account import Account
from sampath.users import User

users: List[User] = []
accounts: List[Account]= []

def find_user_by_nic(nic: str) -> Optional[User]:
    for user in users:
        if nic == user.get_nic():
            return user
    return None

def find_account(accnt_no: str) -> Optional[Account]:
    for account in accounts:
        if account.get_account_no() == accnt_no:
            return account
    return None

def list_all_cheques() -> None:
    cheques = []
    for account in accounts:
        if isinstance(account, CurrentAccount):
            cheques.extend(account.get_cheque_ids())

    print(f"All cheque ids - {cheques}")

if __name__ == '__main__':
    user1 = User("22222V", 21, "Kalana")
    user2 = User("11111V", 22, "Supun")
    users.append(user1)
    users.append(user2)
    accnt1 = SavingsAccount(account_no="232323"
                            , branch="moratuwa", balance=12333.33
                            , user=user1
                            ,atm_card_no="1234 4444 5555 4444")
    accnt2 = CurrentAccount(account_no="44545"
                            , branch="moratuwa", balance=12333.33
                            , user=user2
                            ,cheque_ids=["23232", "123233"])
    accnt3 = CurrentAccount(account_no="zzdzd"
                            , branch="moratuwa", balance=12333.33
                            , user=user2
                            , cheque_ids=["2432444", "34343434"])
    accounts.append(accnt1)
    accounts.append(accnt2)
    print(find_account("44545"))
    print(find_user_by_nic("11111V"))