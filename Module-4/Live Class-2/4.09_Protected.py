# 1:38:00

# Protected------> (_) 1 underscore


class Bank_Account:

    def __init__(self):
        self.__balance = 0                      # Private
        self._type = "Savings"                  # Protected


   

bank1 = Bank_Account()

print(bank1._type)                              # Python won't mind
                                                # Python doesn't Enforce 
                                                # Paite paro but baire theke access koiro na
                                                # access kora uchit na