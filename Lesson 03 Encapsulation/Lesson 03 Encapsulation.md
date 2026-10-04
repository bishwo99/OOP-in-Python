# Lesson 03: Encapsulation

Encapsulation means keeping data and the methods that operate on that data together inside a class and controlling how the data is accessed or modified.

- Public: `name`
- Protected convention: `_name`
- Private: `__name`
- `__name` uses name mangling in Python.
- Private data can be accessed or modified through controlled methods.

Example:
`__balance` is protected from direct external access, while `deposit()`, `withdraw()`, and `show_balance()` provide controlled interaction.