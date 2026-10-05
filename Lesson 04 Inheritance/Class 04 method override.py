class person:
    def introduction(self):
        print('I am a Person')

class student(person):
    def introduction(self):
        print('I am  a student.')

class teacher(person):
    def introduction(self):
        print('I am a teacher')

student1 = student()
teacher1 = teacher()

student1.introduction()
teacher1.introduction()