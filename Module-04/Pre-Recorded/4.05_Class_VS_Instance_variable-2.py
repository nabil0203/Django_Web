class School:

    school_name = "JUSC"                        # Class Varibale

    def __init__(self, name):
        self.student_name = name                # Instance Variable
    

sc1 = School("Nabil")
sc2 = School("Kola")


sc1.school_name = "Savar Cantonment"                # Class variable changed for a specific object (sc1)



print(sc1.school_name, sc1.student_name)
print(sc2.school_name, sc2.student_name)