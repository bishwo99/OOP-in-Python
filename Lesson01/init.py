# Student object তৈরি
#        ↓
# __init__() automatically call
#        ↓
# name = "Bish"
#        ↓
# self.name = "Bish"

class student:
    def __init__(self,name):
        self.name = name
    def intro(self):
        print(f'My name is {self.name}')

student1 = student('Bishwo')
student2 = student('Mr. Saha')

student1.intro()
student2.intro()


