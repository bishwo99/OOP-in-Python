class Cat:
    def sound(self):
        print("Cat says: Meows!!")

class Dog: 
    def sound(self):
        print("Dog says: Woof!!")

class Cow:
    def sound(self):
        print("Cow says: Mooo!!")


animals = [Cat(), Dog(), Cow()]

for animal in  animals:
    animal.sound()