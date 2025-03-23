# Part 1: Basic Python Concepts

# Printing and User Input
print("Hello, World!")  # This prints "Hello, World!" to the console.
name = input("What is your name? ")  # Takes user input as a string.
print("This is {}".format(name))  # Formats the string to insert the user's name.

# Variables and Data Types
num = float(input("Enter num: "))  # Takes user input and converts it to a float.
print("Number is " + str(num))  # Converts the float to a string for concatenation.

# String Operations
string_val = "this is a String"
print(string_val.upper())  # Converts the string to uppercase.
print(string_val.replace("is", "iz"))  # Replaces 'is' with 'iz' in the string.
print("this issss python".find("isss"))  # Finds the index of the substring 'isss'.

# Operators in Python
print(10 // 3)  # Integer division (returns 3).
print(10 / 3)   # Floating point division (returns 3.3333...).
print(10 ** 3)  # Exponentiation (returns 1000).

# Conditional Statements (if-else)
if 1 < 3:
    print("1 is less than 3")
else:
    print("1 is greater than 3")

# Loops
# While loop
i = 0
while i < 5:
    print(i)  # Prints numbers from 0 to 4.
    i += 1  # Increments i by 1 after each iteration.

# For loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)  # Prints each number in the list.

# Lists (Dynamic Arrays)
names = ["Jaimit", "Simran", "SJ"]
print(names[-1])  # Prints the last element in the list.
print(names[0:2])  # Prints the first two elements of the list.

# List Operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
numbers.insert(8, 9)  # Inserts 9 at index 8.
numbers.remove(3)  # Removes the number 3 from the list.
print(3 in numbers)  # Checks if 3 is in the list.
numbers.clear()  # Clears the entire list.
print(len(numbers))  # Prints the length of the list.

# Part 2: Object-Oriented Programming (OOP) Concepts

# OOP Concept 1: Classes and Objects (Encapsulation)
# A class defines the blueprint for an object.

class Car:
    # Constructor (__init__) to initialize the properties of the object
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable to store the car's brand
        self.model = model  # Instance variable to store the car's model

    # Method to display the car's details
    def show_details(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object (instance) of the Car class
car1 = Car("Tesla", "Model S")
car1.show_details()  # Prints: Car: Tesla Model S


# OOP Concept 2: Inheritance (Reusing and Extending Classes)
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Calls the constructor of the parent class (Car)
        self.battery = battery  # Additional property for ElectricCar

    # Method to display the battery capacity
    def show_battery(self):
        print(f"Battery Capacity: {self.battery} kWh")

# Creating an object of the ElectricCar class
ev = ElectricCar("Tesla", "Model 3", 75)
ev.show_details()  # Inherited from Car: Car: Tesla Model 3
ev.show_battery()  # Specific to ElectricCar: Battery Capacity: 75 kWh


# OOP Concept 3: Polymorphism (Same Method Name, Different Behavior)
class Animal:
    def speak(self):
        pass  # Base method, which will be overridden by subclasses

class Dog(Animal):
    def speak(self):
        return "Woof!"  # Dog's version of the speak method

class Cat(Animal):
    def speak(self):
        return "Meow!"  # Cat's version of the speak method

# Creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!


# OOP Concept 4: Abstraction (Hiding Implementation Details)
# An abstract class is a class that cannot be instantiated on its own. It is used to define common methods
# that will be shared by its subclasses.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass  # This method will be implemented by subclasses

class Car(Vehicle):
    def move(self):
        print("The car is moving.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing.")

# Creating objects of Car and Boat
car = Car()
boat = Boat()
car.move()  # The car is moving.
boat.move()  # The boat is sailing.


# Part 3: Advanced Concepts

# Recursion (A function calling itself)
def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    return n * factorial(n - 1)  # Recursive call to calculate factorial

print(factorial(5))  # 120


# Part 4: Data Structures in Python

# Stack (LIFO - Last In First Out)
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
stack.pop()  # Pop the last element (2)
print(stack)  # [1]

# Queue (FIFO - First In First Out)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # Adds 4 to the queue
queue.popleft()  # Removes the first element (1)
print(queue)  # deque([2, 3, 4])


# Linked List (A collection of nodes where each node contains data and a reference to the next node)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Next is initially None, it will point to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # The list is initially empty

    # Method to append a new node to the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If the list is empty, set head to the new node
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse the list to the last node
        last.next = new_node  # Set the next of the last node to the new node

# Creating and appending nodes to the linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)


# Binary Search Tree (BST) - A tree data structure where each node has at most two children
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

# Inserting values into the BST
root = BSTNode(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(7)

# Creating a dictionary (like a HashMap in Java)
person = {
    "name": "Jaimit",
    "age": 25,
    "city": "New York"
}

# Accessing values using keys
print(person["name"])  # Output: Jaimit
print(person["age"])   # Output: 25

# Adding a new key-value pair
person["profession"] = "Developer"

# Updating a value
person["age"] = 26

# Removing a key-value pair
del person["city"]

# Checking if a key exists
if "name" in person:
    print("Name exists in dictionary")

# Using the get() method (similar to HashMap.get() in Java)
print(person.get("profession"))  # Output: Developer
print(person.get("address", "Not Found"))  # Output: Not Found (default value if key doesn't exist)


# Explanation of Code Concepts:
# Python Basics:

# Input and Output: print() is used to display output, and input() is used to take user input.

# Variables and Types: Variables can hold values of different types, such as integers, strings, and floats.

# Control Flow: if-else is used for decision-making, and loops (while and for) are used for repetitive tasks.

# Data Structures: Lists and tuples are used to store collections of items. Lists are mutable, and tuples are immutable.

# Object-Oriented Programming (OOP):

# Classes and Objects: A class is a blueprint for creating objects. The __init__ method is a constructor used to initialize object properties.

# Inheritance: A subclass can inherit properties and methods from a parent class. super() allows a subclass to call methods of the parent class.

# Polymorphism: Different objects can share the same method name but provide different implementations.

# Abstraction: Abstract classes cannot be instantiated directly but can define methods that must be implemented by subclasses.

# Recursion:

# A function that calls itself is a recursive function. It is useful for problems that can be broken down into smaller subproblems, like calculating factorials.

# Data Structures:

# Stack: A stack is a collection that follows Last In First Out (LIFO) order. It uses append() to add and pop() to remove items.

# Queue: A queue is a collection that follows First In First Out (FIFO) order. It uses append() to add and popleft() to remove items.

# Linked List: A linked list is a series of nodes, where each node contains data and a reference to the next node.

# Binary Search Tree (BST): A BST is a tree where each node has at most two children, and the left child is smaller than the parent while the right child is larger.