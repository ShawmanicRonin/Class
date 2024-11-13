#Class is a blueprint of an object
class Student:
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'
    def print_student_data(self):
        print(f"Student Info \n",
              f"First Name: {self.first_name} \n",
              f"Last Name: {self.last_name} \n",
              f"Grade: {self.grade} \n",
              f"Email: {self.email}\n")
    def change_grade(self, new_grade_lvl):
        #TODO change grade lvl
        self.grade = new_grade_lvl


#jay_pike is an instance of the student class
jay_pike = Student("Jay", "Pike", "Sophomore") #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior") #object of the student class
waldo_wildcat = Student('Waldo', 'Wildcat', 'Senior')

# print(jay_pike.email)
# print(jane_doe.email)
# print(waldo_wildcat.email)

jay_pike.print_student_data()
jane_doe.print_student_data()
waldo_wildcat.print_student_data()

jay_pike.change_grade("Junior")
jane_doe.change_grade("Graduate")
waldo_wildcat.change_grade("Freshman")

jay_pike.print_student_data()
jane_doe.print_student_data()
waldo_wildcat.print_student_data()