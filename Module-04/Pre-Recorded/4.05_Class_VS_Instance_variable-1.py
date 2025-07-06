class School:

    school_name = "JUSC"                        # Class Varibale        (Exactly Same for each object)

    def __init__(self, name):
        self.student_name = name                # Instance Variable         (Unique for each object)
    

sc1 = School("Nabil")
sc2 = School("Kola")


print(sc1.school_name, sc1.student_name)
print(sc2.school_name, sc2.student_name)