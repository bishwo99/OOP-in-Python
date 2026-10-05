# ## Exercise 01: Implementing Multilevel Inheritance in Python

# **Course:** Object-Oriented Programming (Python)  
# **Topic:** Inheritance  
# **Difficulty:** Beginner  
# **Marks:** 10

# ### Problem Statement

# A software development company is designing an animal classification system using Object-Oriented Programming (OOP).
# The system must demonstrate **Multilevel Inheritance** by creating three classes: `Animal`, `Mammal`, and `Dog`.

# Implement the system according to the following specifications.

# ### Requirements

# 1. Create a parent class named `Animal` containing an `eat()` method that displays `Animal is eating.`
# 2. Create a class named `Mammal` that inherits from `Animal` and defines a `walk()` method that displays `Mammal is walking.`
# 3. Create a class named `Dog` that inherits from `Mammal` and defines a `bark()` method that displays `Dog is barking.`
# 4. Instantiate an object of the `Dog` class and use it to invoke all three methods.
# 5. Add a comment identifying the type of inheritance implemented.

# ### Expected Output

# ```text
# Animal is eating.
# Mammal is walking.
# Dog is barking.
# ```

# ### Mark Distribution

# | Assessment Criteria | Marks |
# |---|---:|
# | Correct implementation of `Animal` | 2 |
# | Correct implementation of `Mammal` | 2 |
# | Correct implementation of `Dog` | 2 |
# | Proper object creation and method calls | 3 |
# | Correct identification of inheritance type | 1 |
# | **Total** | **10** |

# **Instruction:** Write a complete Python program following proper class naming conventions. Do not modify the expected output.


class Animal:
    def eat(self):
        print('Animal is eating.')

class Mammal(Animal):
    def walk(self):
       # super().eat()
        print('Mammal is walking.')

class Dog(Mammal):
    def bark(self):
        #super().walk()
        print('Dog is barking.')

dog = Dog()
dog.eat()
dog.walk()
dog.bark()

# Multilevel Inheritance