class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def introduction(self):
        print(f"Hi, I am {self.name} and my age is {self.age}.")

class Student(Person):
    def study_subject(self,name): # Child can contain atrributes too.. 
        self.name = name 
        print(f"I'm studying {self.name}.")

student1 = Student('Bishwo',25)
student1.introduction()
student1.study_subject('OOP in Python')
    