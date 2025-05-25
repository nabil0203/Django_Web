
class Currency_Converter:
    
    # Class Attributes
    exchange_rate = {
        "USD" : 1.00,                   # USD base value
        "BDT" : 121.75,
        "EUR" : 0.88,
        "GBP" : 0.75
    }



    # Instance Attribute
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()



    # Instance Method--->Handles Conversion
    # Instance method used to handle each kind of object indivisually. It makes it Dynamic
    def convert(self):
        if self.from_currency not in Currency_Converter.exchange_rate or \
            self.to_currency not in Currency_Converter.exchange_rate:

            return "Invalid Currency!!! Not availale in this Conversion"
        
        

        '''
        - Always convert Any Currency into USD first then convert USD into the Desired currency
        - if, (500 BDT --> EUR) conversion
        - at first (500 BDT-->USD) after that (USD--->EUR)
        '''

        base_amount = self.amount / Currency_Converter.exchange_rate[self.from_currency]                                        # base_amount = 500 BDT / 121.75
        converted_amount = base_amount * Currency_Converter.exchange_rate[self.to_currency]                                     # converted_amount =  base_amount * .88

        return round(converted_amount,2)


    
    # Class method--->Updates Exchange rate
    # Direct action performed on the Class Arrtibutes, that's why class mmethod needed
    @classmethod
    def update_rate(cls, currency, new_rate):
        cls.exchange_rate[currency] = new_rate



    # Static method(not mandatory to use)---> Checks if the currency is valid or not
    @staticmethod
    def is_valid_currency(user_given_currency):
        return user_given_currency.upper() in Currency_Converter.exchange_rate

    





class Logger:                                               # this class holds the record of the conversion of differnt users(Association relation)

    # Instance Method
    def log(self, user, converter):
        result = converter.convert()
        print(f"Record: {user} converted {converter.amount} {converter.from_currency} --> {result} {converter.to_currency}")




if __name__ == "__main__":
    
    user = input("Enter your Name: ")
    amount = float(input("Enter amount: "))
    from_curr = input("Enter your Currency: ")
    to_curr = input("Enter Desired Currency: ")


    converter = Currency_Converter(amount, from_curr,  to_curr)                              # object


    if not Currency_Converter.is_valid_currency(from_curr) or \
        not Currency_Converter.is_valid_currency((to_curr)):

        print("Invalid Currency!!! Not availale in this Conversion")

    
    else:
        logger_obj = Logger()
        logger_obj.log(user, converter)