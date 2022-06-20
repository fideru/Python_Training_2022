# Classes are blueprints for creating new objects
# Objects are instances of said class

# Class: Human, Animal
# Objects: John, Mary, Cat, Dog
# Creating a class use pascal naming convention.
# attributes in a class can be instance level to be defined each time an object is created
# and class level to be used by all objects each time one is defined
import self as self


class Point:

    # Class level attributes
    default_color = "Blue"
    # Magic methogs use __ and are called by python always.
    # Magic method called constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Comparing magic methods eq = equal to, gt = greater than etc
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Class Method Creation
    @classmethod # Class Decorator to extend the behaviour of a method of function
    def zero(cls):
        return cls(0, 0)
    # Add functions related to the class to be used by the objects
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

###############################################
point_object = Point.zero()
point_object.draw()
# Comparing objects with magic methods
point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)
print(point1 > point2)
# Evaluate if said object is an instance of said class
print(type(point_object))
print(isinstance(point_object, Point))
print(point_object.x)



##################
# Container types

class TagCloud:
    # Constructor Initial lass
    def __init__(self):
        self.__tags = {}

    # Magic metod to add tags to object in class
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # Magic method to read quantity of given tag
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # Magic method to set the number of times a given tag exist
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # Magic method to see lenght of tags
    def __len__(self):
        return len((self.__tags))

    # Magic method to iterate over tag
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PYThon")
print(cloud.__dict__)

###################################################
# PROPERTIES is an object that sits in front of an attribute and allows you to get/set its value
# you can make functions private in class by adding __ in front of the name
# Using a decorator to privatice or propertice a function as well
class Product():
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
product = Product(50)

###################################################
# INHERITANCE
# Programming must try at most to be DRY (Dont Repeat Yourself)
# Every class in python derives from the object class in python
# Parent Class
# Method Overriding is the usage of a constructor in a subclass to override the parent constructor
# super() gets the constructor on the parent class for the subclass in case of overriding
# Regarding multilevel inheritance try no to pass over 2 levels of inheritance
# Regarding multiple ingeritance is better to use it only if inherit from 2 or 3 different classes
class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")

# Child/Sub class
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 1
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swin")

class Bird(Animal):
    def fly(self):
        print("fly")
# Bad inheritance cuz chickens cannot fly G
class Chicken(Bird):
    pass

#########################################
# Good Inheritance
# Abstract Base Classes

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOperationError("The stream is already open")
        self.opened = True
    def close(self):
        if self.opened:
            raise InvalidOperationError("The Stream is already closed")
        self.opened = False
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


#########################################
# Polymorphism
# Means that a specific class or method takes many forms.
# Python doesnt check for the type of object just for if its there or not
# This is Duck Typing

class UIControl(ABC):
    def draw(self):
        print("Draw")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")
class TextBox(UIControl):
    def draw(self):
        print("TextBox")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

#########################################
# Extending Built-in Types
# Built in Types are also usable for inheritance str, int, float etc

class Text(str):
    def duplicate(self):
        return self + self

class TrackableList(list):
    def append(self, __object):
        print("Append called")
        super().append(object)

tesxt = Text("Python")
print(tesxt.duplicate())
