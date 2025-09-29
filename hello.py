# This is first Python script
print("Hello world!")

# Variables and Data types
x = 10  # integer
y = 3.14  # float
name = "Alice"  # string
is_student = True  # boolean
print("x =", x)
print("y =", y)
print("name =", name)
print("is_student =", is_student)

# Conditional statements
marks = 75
if marks == 100:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("F")

# While Loop
counter = 0
while counter != 5:
    counter += 1
    print("Counter is", counter)

# For loop
for i in range(5):
    print("i is", i)

# List operations
myList = [1, 2, 3, 4, 5]
print("My list is", myList)
myList.append(6)
print("My list is now", myList)
myList.remove(2)
print("My list after remove", myList)
myList.pop()
print("My list after pop", myList)
myList.insert(1, 10)
print("My list after insert", myList)
myList.sort()
print("My list after sort", myList)
myList.reverse()
print("My list after reverse", myList)
print("Length of my list is", len(myList))

# Dictionary operations : key-value pairs
myDict = {"name": "John", "age": 30, "city": "New York"}
print("My dictionary is", myDict)
print("Name is", myDict["name"])
myDict["age"] = 31
print("My dictionary after update", myDict)

# String operations
word = "Python"
print(word[0:3])  # prints 'Pyt'
print(word[3:])  # prints 'hon'
print(word[:3])  # prints 'Pyt'
print(word[-1])  # prints 'n'
print(word[-3:])  # prints 'hon'
print(word.upper())  # prints 'PYTHON'
print(word.lower())  # prints 'python'
print(word.replace("P", "J"))  # prints 'Jython'
print("Length of word is", len(word))

# Tuple operations : immutable list
myTuple = (1, 2, 3, 4, 5)
# myTuple[0] = 10 # This will raise an error
print("My tuple is", myTuple)
print("Length of my tuple is", len(myTuple))
print("First element of my tuple is", myTuple[0])

# Operators
a = 10
b = 3
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a**b)  # Exponentiation
print("a == b is", a == b)  # Equal to
print("a != b is", a != b)  # Not equal to
print("a > b is", a > b)  # Greater than
print("a < b is", a < b)  # Less than
print("a >= b is", a >= b)  # Greater than or equal to
print("a <= b is", a <= b)  # Less than or equal to
print("a and b is", a and b)  # Logical AND
print("a or b is", a or b)  # Logical OR
print("not a is", not a)  # Logical NOT

print("Data type of a is", type(a))

# Set operations
mySet = {4, 2, 1, 9, 5, 4, 5}
print("My set is", mySet)
mySet.add(6)
print("My set after add 6 is ", mySet)
mySet.remove(2)
print("My set after remove 2 is ", mySet)
mySet.pop()
print("My set after pop", mySet)
print("Length of my set is", len(mySet))
mySet.clear()
print("My set after clear is", mySet)


# Function definition and call
def addNumber(number1, number2):
    return number1 + number2


result = addNumber(10.52, 20.30)
print("Result of addNumber is", result)  # 30.82
print("Floor", result.__floor__())  # 30
print("Ceil", result.__ceil__())  # 31
print("Round", result.__round__())  # 31


# Tuple return from function
def get_name_and_age():
    name = "Vijay"
    age = 25
    return name, age


name, age = get_name_and_age()
print("Name is", name)
print("Age is", age)


# Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


p1 = Person("Amit", 30)
p1.display()

# Two Dimensional Array
twoDArray = [[1, "One"], [2, "Two"], [3, "Three"]]
for row in twoDArray:
    for col in row:
        print(col, end=" ")
    print()

# ========== Output

"""
python3 hello.py

Hello world!
x = 10
y = 3.14
name = Alice
is_student = True
B
Counter is 1
Counter is 2
Counter is 3
Counter is 4
Counter is 5
i is 0
i is 1
i is 2
i is 3
i is 4
My list is [1, 2, 3, 4, 5]
My list is now [1, 2, 3, 4, 5, 6]
My list after remove [1, 3, 4, 5, 6]
My list after pop [1, 3, 4, 5]
My list after insert [1, 10, 3, 4, 5]
My list after sort [1, 3, 4, 5, 10]
My list after reverse [10, 5, 4, 3, 1]
Length of my list is 5
My dictionary is {'name': 'John', 'age': 30, 'city': 'New York'}
Name is John
My dictionary after update {'name': 'John', 'age': 31, 'city': 'New York'}
Pyt
hon
Pyt
n
hon
PYTHON
python
Jython
Length of word is 6
My tuple is (1, 2, 3, 4, 5)
Length of my tuple is 5
First element of my tuple is 1
a + b = 13
a - b = 7
a * b = 30
a / b = 3.3333333333333335
a // b = 3
a % b = 1
a ** b = 1000
a == b is False
a != b is True
a > b is True
a < b is False
a >= b is True
a <= b is False
a and b is 3
a or b is 10
not a is False
Data type of a is <class 'int'>
My set is {1, 2, 4, 5, 9}
My set after add 6 is  {1, 2, 4, 5, 6, 9}
My set after remove 2 is  {1, 4, 5, 6, 9}
My set after pop {4, 5, 6, 9}
Length of my set is 4
My set after clear is set()
Result of addNumber is 30.82
Floor 30
Ceil 31
Round 31
Name is Vijay
Age is 25
Name: Amit
Age: 30
1 One 
2 Two 
3 Three 
"""
