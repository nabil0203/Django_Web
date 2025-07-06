# 1:42:00


# Child replaces some properties inherited from the parent



class Bank_Account:
    def withdraw_money(self):                               # same method name
        print("sb TAKA uthay felci vayaaaaaaaa")


class Savings_account(Bank_Account):
    def withdraw_money(self):                               # same method name
        print("TAKA NAIIIII")




bank1 = Bank_Account()
bank1.withdraw_money()                                  # method called through object---> bank1


save1 = Savings_account()
save1.withdraw_money()                                  # method called through object---> save1