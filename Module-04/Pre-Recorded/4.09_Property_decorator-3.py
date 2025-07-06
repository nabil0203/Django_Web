# Property Decorator


class Employee:
    company_name = "Ostad Platform"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary



    @property
    def salary(self):                             # method name changed (_salary --> salary)
        return self._salary
    

    @salary.setter                                # setter method
    def salary(self, new_salary):
        self._salary = new_salary



obj1 = Employee("Rahim", 44000)



print(obj1.salary)                              # 44000 --->calling through 'salary'

obj1.salary = 77000                             # Setting new salary

print(obj1.salary)                              # 77000
