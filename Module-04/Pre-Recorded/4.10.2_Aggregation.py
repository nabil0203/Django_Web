# Aggregation
# has a realtionship
# University has Departments
# Classes can operate independently


class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.deparments = []

    def add_department(self, department):
        self.deparments.append(department)

    def show_departments(self):
        return [department.name for department in self.deparments]                   # It creates and returns a list of names of all departments stored in self.departments
    


uni1 = University("DIU")
dep1 = Department("CSE")
dep2 = Department("SWE")

uni1.add_department(dep1)                   # passing object dep1
uni1.add_department(dep2)                   # passing object dep2

print(uni1.show_departments())
    


