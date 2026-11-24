class Student:
    def show(self):
        print("Student: Shrikrushna")

class Teacher(Student):
    def show(self):
        print("Teacher: ABC")

s = Student()
t = Teacher()

s.show()
t.show()
