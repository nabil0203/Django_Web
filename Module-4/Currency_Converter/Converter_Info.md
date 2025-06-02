# 🎯 Project: Currency Converter CLI App


This project is a `CLI-based` app that takes user input and performs real-time currency conversion (using mock rates).

Here Python OOP has been to create a realistic Currency Converter application.

----
File name: `currency_converter.py`
---

### **CurrencyConverter Class**:
- A `class attribute` must store all the exchange rates for various currencies.
- It should have instance attributes: `amount`, `from_currency`, and `to_currency`, which should be initialized through the `__init__` method.
- It must include an `instance method` that performs the currency conversion.
- It must include a `class method` that updates the exchange rates.
- It must include a `static method` that validates whether a given currency code is valid.

---

### **Logger Class** (Association Demonstration):

- This should be a completely `separate class`.
- It must include a method named `log` (user, amount, result) that logs the user’s conversion details.
- An object of the Logger class should not be created inside the CurrencyConverter class.
- Instead, the CurrencyConverter class should accept a Logger object as input from outside, forming an association relationship between the two classes.
---