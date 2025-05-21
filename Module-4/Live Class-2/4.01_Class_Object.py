# 26:00


class Student:
    def __init__(self, name, mark):
        self.student_name = name
        self.student_mark = mark

    def add_mark(self, n):
        self.student_mark = self.student_mark + n
    
    def show_mark(self):
        print(f"{self.student_name} has {self.student_mark} mark")



student1 = Student("Nabil", 98)
student2 = Student("Ahmed", 34)
student3 = Student("Chowdhury", 77)


student1.show_mark()
student1.add_mark(20)
student1.show_mark()

student2.show_mark()