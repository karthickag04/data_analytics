"""
Data Structures in Python
=========================
Python provides several built-in data structures to store collections of data. The most commonly used are lists, tuples, sets, and dictionaries.

1. Lists
2. Tuples
3. Sets
4. Dictionaries
"""

"""
1. Lists
---------
- Lists are ordered, mutable collections of items.
- They allow duplicate elements.

Creating a list:
"""
# Creating a list
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Accessing elements
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# Modifying elements
fruits[1] = "blueberry"
print("Modified list:", fruits)

# Adding elements
fruits.append("date")
print("List after append:", fruits)
fruits.insert(1, "banana")
print("List after insert:", fruits)

# Removing elements
fruits.remove("banana")
print("List after remove:", fruits)
removed_element = fruits.pop()
print("List after pop:", fruits)
print("Removed element:", removed_element)

# Other list methods
fruits.extend(["elderberry", "fig", "grape"])
print("List after extend:", fruits)
fruits.sort()
print("Sorted list:", fruits)
fruits.reverse()
print("Reversed list:", fruits)
print("Index of 'cherry':", fruits.index("cherry"))
print("Count of 'apple':", fruits.count("apple"))

# List comprehension
squares = [x**2 for x in range(10)]
print("Squares using list comprehension:", squares)

"""
2. Tuples
---------
- Tuples are ordered, immutable collections of items.
- They allow duplicate elements.

Creating a tuple:
"""
# Creating a tuple
fruit_tuple = ("apple", "banana", "cherry")
print("Tuple:", fruit_tuple)

# Accessing elements
print("First element:", fruit_tuple[0])
print("Last element:", fruit_tuple[-1])

# Tuples are immutable, so we can't modify elements directly.
# However, we can create a new tuple by concatenation or repetition.
new_tuple = fruit_tuple + ("date",)
print("New tuple after concatenation:", new_tuple)

repeated_tuple = fruit_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Tuple methods
print("Index of 'banana':", fruit_tuple.index("banana"))
print("Count of 'apple':", fruit_tuple.count("apple"))

"""
3. Sets
-------
- Sets are unordered collections of unique elements.
- They do not allow duplicate elements.

Creating a set:
"""
# Creating a set
fruit_set = {"apple", "banana", "cherry"}
print("Set:", fruit_set)

# Adding elements
fruit_set.add("date")
print("Set after add:", fruit_set)

# Removing elements
fruit_set.remove("banana")
print("Set after remove:", fruit_set)
fruit_set.discard("fig")  # No error if element not found
print("Set after discard:", fruit_set)
popped_element = fruit_set.pop()  # Removes a random element
print("Set after pop:", fruit_set)
print("Popped element:", popped_element)

# Other set methods
fruit_set.update({"elderberry", "fig", "grape"})
print("Set after update:", fruit_set)
print("Length of set:", len(fruit_set))
print("Is 'cherry' in set?", "cherry" in fruit_set)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

"""
4. Dictionaries
---------------
- Dictionaries are unordered collections of key-value pairs.
- Keys must be unique and immutable.

Creating a dictionary:
"""
# Creating a dictionary
student = {"name": "John", "age": 21, "course": "Data Science"}
print("Dictionary:", student)

# Accessing elements
print("Name:", student["name"])

# Modifying elements
student["age"] = 22
print("Modified dictionary:", student)

# Adding elements
student["grade"] = "A"
print("Dictionary after adding element:", student)

# Removing elements
del student["course"]
print("Dictionary after deleting 'course':", student)
grade = student.pop("grade")
print("Dictionary after popping 'grade':", student)
print("Popped value:", grade)

# Other dictionary methods
student.update({"course": "Data Science", "grade": "A"})
print("Dictionary after update:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Looping through dictionary
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print("Squares using dictionary comprehension:", squares_dict)
