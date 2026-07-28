from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def department(self):
        pass

class CSEStudent(Student):
    def department(self):
        print("Department: Computer Science and Engineering")

s = CSEStudent()
s.department()
