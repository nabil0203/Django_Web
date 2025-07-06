# 39:00 
# 'self' ---> attaches the variable with the object



class Student:
    def __init__(self):
        name = "Nabil"                      # self not used
        self.mark = 54                      # self used



student1 = Student()


print(student1.mark)                     # 54    ---> 'self' used, so 'mark' is attached to the object 'student1'
print(student1.name)                     # ERROR ---> bcz 'student1' object doesn't have 'name'
