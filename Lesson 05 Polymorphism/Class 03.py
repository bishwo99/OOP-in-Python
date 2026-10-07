# Duck Typing
# Python-e ekta famous idea ache:
# "If it walks like a duck and it quacks like a duck, then it is a duck."

# Programming-e er meaning holo:
# Object-ta kon class-er, seta niye beshi important na. Object-er required method ache kina, seta important.


class Cat:
    def sound(self):
        print('Meow!')

class Dog:
    def sound(self):
        print("Woof!!")


def make_sound(animal):
    animal.sound()


cat = Cat()
dog = Dog()

make_sound(cat)
make_sound(dog)