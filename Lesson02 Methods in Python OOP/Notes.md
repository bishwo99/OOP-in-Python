# Lesson 02: Methods in Python OOP

## Instance Method
- Uses `self`.
- Works with a specific object's data.
- Example: `intro(self)`

## Class Method
- Uses `cls`.
- Works with class-level data.
- Uses `@classmethod`.
- Example: `show_university(cls)`

## Static Method
- Does not use `self` or `cls`.
- Performs an independent operation related to the class.
- Uses `@staticmethod`.
- Example: `is_valid_id(candidate_id)`

### Easy Reminder

self → Object
cls → Class
neither → Static Method

Instance Method → self ব্যবহার করে specific object-এর data নিয়ে কাজ করে।
Class Method → cls ব্যবহার করে class-level data নিয়ে কাজ করে।
Static Method → self/cls ছাড়াই class-এর সাথে logically related independent কাজ করে।