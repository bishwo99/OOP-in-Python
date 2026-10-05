# Lesson 04: Inheritance in Python

Inheritance is one of the most important concepts of Object-Oriented Programming (OOP).

It allows one class to reuse the properties and methods of another class.

---

# 1. What is Inheritance and Why Do We Use It?

## What is Inheritance?

Inheritance is an OOP mechanism where a **Child Class** acquires the attributes and methods of a **Parent Class**.

In simple words:

> A child class can reuse the functionality of its parent class.

The parent class is also called:

- Base Class
- Superclass

The child class is also called:

- Derived Class
- Subclass

### Basic Syntax

```python
class Parent:
    pass


class Child(Parent):
    pass

Most Important Things to Remember
1. class Child(Parent) creates inheritance.
2. A child class can reuse parent methods and attributes.
3. A child class can have its own methods.
4. If the child has no __init__(), it can use the parent's __init__().
5. If the child has its own __init__(), the parent's __init__() does not automatically execute.
6. super() is used to access parent functionality.
7. super() does not create inheritance.
8. Method overriding means the child provides its own version of a parent method.
9. super() can be used in overriding when we want both parent and child behavior.
10. The four main types of inheritance are Single, Multilevel, Hierarchical, and Multiple.