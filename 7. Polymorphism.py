class Student:
    def introduction(self):
        print("I am a student.")

class CSEStudent(Student):
    def introduction(self):
        print("I am a CSE student.")

class AIMLStudent(Student):
    def introduction(self):
        print("I am an AIML student.")

students = [Student(), CSEStudent(), AIMLStudent()]

for s in students:
    s.introduction()
