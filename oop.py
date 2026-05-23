
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
