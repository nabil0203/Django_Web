# Property Decorator


class Employee:
    company_name = "Ostad Platform"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary                   # We want, Anyone can see the Salary but not Edit/Update it (make Read-only)




    @property                                   # this works as Getter method
    def get_salary(self):                         
        return self._salary
    



obj1 = Employee("Rahim", 44000)

print(obj1._salary)                             # 4400
print(obj1.get_salary)                          # 4400     --> this method works as a Variable


obj1._salary = 77000
print(obj1._salary)                             # 77000
                                                # here the salary is updating
                                                # it's not read-only yet