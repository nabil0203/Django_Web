

class Bank_Account:
    def withdraw_money(self):
        print("Money Withdrawn")


class Savings_account(Bank_Account):                       # Savings_account inherits Bank_Account
    def haha(self):
        print("hahahaha")


class Current_Account(Savings_account):                    # Current_Account inherits Savings_account
    def lala(self):
        print("Lalalalala")



cur1 = Current_Account()
cur1.lala()
cur1.withdraw_money()
cur1.haha()