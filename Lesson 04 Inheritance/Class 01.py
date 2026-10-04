class Person:
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def intro(self):
        print(f"Hey,My name is {self.name} and i am from {self.location}!")

class Student(Person):  # Ekhane Person class ta Student class inherit koreche.
    pass

student1 = Student('Bishwojit', 'Jhenaidah')

student1.intro()
