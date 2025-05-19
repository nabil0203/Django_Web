class Employee:
    company_name = "Ostad Platform"

    def __init__(self, name, salary):                           # constructor
        self.name = name
        self.salary = salary


    def display_info(self):                                     # Instance Method
        print("Employee name: ", self.name)
        print("Salary: ", self.salary)

     
    @classmethod                                              # Class Method
    def change_company_name(cls, name):                                # 'cls' used inside parameter
        cls.company_name = name                                        # '@classmethod' decorator--> it's declares that it's a class method




obj1 = Employee("Rahim", 30000)
obj2 = Employee("Khoka", 98223)
obj1.display_info()
obj2.display_info()



print(obj1.company_name)                                            # Ostad Platform

Employee.change_company_name("Amar baper company")                  # From Here, company changed for whole class

print(obj1.company_name)                                            # Amar baper company
print(obj2.company_name)                                            # Amar baper company