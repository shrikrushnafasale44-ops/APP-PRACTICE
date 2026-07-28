class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name

    def show_department(self):
        print("Department:", self.dept_name)

class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print("Student Name:", self.name)
        self.department.show_department()

dept = Department("Computer Science and Engineering")
student = Student("Shrikrushna", dept)

student.display()
