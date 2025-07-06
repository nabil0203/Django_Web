# Property Decorator


class Employee:
    company_name = "Ostad Platform"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary




    @property
    def _salary(self):                          # funtion name change--> as same as the '_salary' variable
        return self._salary
    



obj1 = Employee("Rahim", 44000)

print(obj1._salary)
print(obj1.get_salary)


obj1._salary = 77000
print(obj1._salary)                             # ERROR -----> bcz the Method name is same as the Variable
                                                # it's now read only, can't update it
                                                # Now we need setter method to set new salary