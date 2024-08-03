"""
Basics of List, Dictionaries, and Tuple
=======================================

List:
-----
- Lists are ordered, mutable collections of items.
- They are defined using square brackets [].

Examples:
"""
# List example
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
fruits.append("orange")
print("Updated List:", fruits)

"""
Dictionary:
-----------
- Dictionaries are unordered, mutable collections of key-value pairs.
- They are defined using curly braces {}.

Examples:
"""
# Dictionary example
student = {"name": "John", "age": 20, "course": "Data Science"}
print("Dictionary:", student)
student["age"] = 21
print("Updated Dictionary:", student)

"""
Tuple:
------
- Tuples are ordered, immutable collections of items.
- They are defined using parentheses ().

Examples:
"""
# Tuple example
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("First color:", colors[0])
