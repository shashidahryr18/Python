class Car:
    # Constructor to initialize the object
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method to describe the car
    def car_details(self):
        return f"Car: {self.brand}, Model: {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla")
print(my_car.car_details())  

#Class with Methods and Attributes
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate area
    def area(self):
        return self.width * self.height

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an object
rect = Rectangle(10, 5)

# Accessing methods
print(f"Area: {rect.area()}")  # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Create an account
account = BankAccount("John", 1000)
account.deposit(500)
print(account.get_balance())  # 
account.withdraw(700)
print(account.get_balance())  # 

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."

# Dog class inherits from Animal class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Cat class inherits from Animal class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # 
print(cat.speak())  #

class Polygon:
# method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

from abc import ABC, abstractmethod  #
# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")#

#Postlab Exercise
#1

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")


#2a
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)


book1 = Book("signals and system", "Anand kumar", 599)
book2 = Book("Data Structures in C", "Yedidyah Langsam", 459)

print("Book Details:")
book1.display_details()
book2.display_details()

#2b
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount
        print(f"Discount of {discount_percent}% applied successfully!")


# Create a book
book1 = Book("COA", "william stallings", 587)

print("Before Discount:")
book1.display_details()

# (b) Apply 10% discount
book1.apply_discount(10)

print("\nAfter Applying 10% Discount:")
book1.display_details()
