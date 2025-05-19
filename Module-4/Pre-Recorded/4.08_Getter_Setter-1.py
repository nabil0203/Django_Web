# Access Control


class Employee:
    company_name = "Ostad Platform"

    def __init__(self, name, salary):
        self.name = name                            # Anyone Can access
        self._salary = salary                       # '._variableName'---> this makes the varibale partially private(protected)
                                                    #  So none can access Salary directly
                                                    #  to access it-------> getter and setter needed


obj1 = Employee("Rahim", 33000)
obj2 = Employee("Karim", 98800)

obj1._salary = 44000
print(obj1._salary)                               # but here we can update the salary of obj1
                                                  # So We need Setter and Getter Method