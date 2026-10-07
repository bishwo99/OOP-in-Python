#Same interface/method name, but different behavior.

class Dog:

    def sound(self):
        print('Dog says: Woof!!') 

class Cat:
    def sound(self):
        print('Cat says: Meow!!')

cat = Cat()
dog = Dog()

cat.sound()
dog.sound()