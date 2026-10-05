class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hi, My name is {self.name} and i am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept
    def department(self):
        print(f"I am from {self.dept} department.")


student1 = Student('Bishwojit',25,'CSE')

student1.introduction()