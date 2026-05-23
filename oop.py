
# 1
class Person:
    def __init__(self, age=0):
        self._age = age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Возраст не может быть отрицательным")
    

    def get_age(self):
        return self._age
    



p = Person()
p.set_age(25) 
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Должна быть ошибка или предупреждение


# 2

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"



class Cat(Animal):
    def speak(self):
        return "Meow"
    
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow


# 3

class Vehicle():

    def move(self):
        return "Vehicle is moving"
    
class Car(Vehicle):
    def move(self):
        return "Car is driving"
    
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()

print(move(car))  # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling


# 4

from abc import ABC, abstractmethod
import math

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,  width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
       return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())