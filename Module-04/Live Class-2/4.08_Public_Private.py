# 1:33:00

# Private------> (__) 2 underscores
# Public ------> Nothing



class Bank_Account:

    def __init__(self):
        self.__balance = 0                      # Private
        self.type = "Savings"                   # Public


    def cash_in(self, taka):
        self.__balance += taka                  # private


    def show_balance(self):
        print(self.__balance)                   # private



bank1 = Bank_Account()


# print(bank1.__balance)                        # not accessible bcz Private can't be accessed from outside object 

bank1.cash_in(500)                              # even though it's Private, it's accessible, bcz the variable is inside the object
bank1.show_balance()                            # even though it's Private, it's accessible, bcz the variable is inside the object