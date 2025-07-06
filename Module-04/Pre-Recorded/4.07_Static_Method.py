# Works as a Normal Method
# Organizes the code


class School:
    school_name = "Amr School"


    @staticmethod
    def calculate_grade(marks):

        if marks >= 90:
            return "A+"
        else:
            return "F"



print(School.calculate_grade(94))
print(School.calculate_grade(54))
