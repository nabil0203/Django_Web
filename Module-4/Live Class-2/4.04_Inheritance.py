# 1:00:00

# A child gets copy of everything the parent offer


class Bank_Account:
    def withdraw_money(self):
        print("Money Withdrawn")


class Savings_account(Bank_Account):                    # Savings_account inherits Bank_Account
    def haha(self):
        print("hahahaha")


class Current_Account(Bank_Account):                    # Current_Account inherits Bank_Account
    def lala(self):
        print("Lalalalala")


save1 = Savings_account()
save1.haha()
save1.withdraw_money()


cur1 = Current_Account()
cur1.lala()
cur1.withdraw_money()