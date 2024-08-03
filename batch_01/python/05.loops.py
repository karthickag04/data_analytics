"""
Loops in Python
===============

- Loops are used to repeatedly execute a block of code as long as a condition is true.
- Python supports two main types of loops: `for` loops and `while` loops.

For Loop:
---------
- The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).
- It executes the block of code multiple times, once for each item in the sequence.

Syntax:
-------
for item in sequence:
    # Block of code

Examples:
"""
# Example of a for loop iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example of a for loop with a range
for i in range(5):
    print("Iteration:", i)

"""
While Loop:
-----------
- The `while` loop is used to execute a block of code as long as a condition is true.

Syntax:
-------
while condition:
    # Block of code

Examples:
"""
# Example of a while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

"""
Nested Loops:
-------------
- Nested loops are loops inside another loop. The inner loop will be executed one time for each iteration of the outer loop.

Examples:
"""
# Example of nested for loops
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)

# Example of nested while loops
i = 0
while i < 3:
    j = 0
    while j < 2:
        print("i:", i, "j:", j)
        j += 1
    i += 1

"""
Break and Continue Statements:
------------------------------
- The `break` statement is used to exit the loop before it has finished iterating over all items.
- The `continue` statement is used to skip the current iteration and continue with the next iteration.

Examples:
"""
# Example of break statement
for i in range(10):
    if i == 5:
        break
    print("Break Example:", i)

# Example of continue statement
for i in range(10):
    if i == 5:
        continue
    print("Continue Example:", i)

"""
Loop with Else:
---------------
- The `else` block will be executed when the loop has finished iterating over all items or the condition becomes false.
- If the loop is terminated by a `break` statement, the `else` block will not be executed.

Examples:
"""
# Example of for loop with else
for i in range(5):
    print("For Loop with Else:", i)
else:
    print("Loop finished")

# Example of while loop with else
count = 0
while count < 5:
    print("While Loop with Else:", count)
    count += 1
else:
    print("Loop finished")

"""
Iterating over Dictionaries:
----------------------------
- You can use a for loop to iterate over the keys, values, or key-value pairs of a dictionary.

Examples:
"""
# Example of iterating over dictionary keys
student = {"name": "John", "age": 21, "course": "Data Science"}
for key in student:
    print("Key:", key, "Value:", student[key])

# Example of iterating over dictionary items
for key, value in student.items():
    print("Key:", key, "Value:", value)
