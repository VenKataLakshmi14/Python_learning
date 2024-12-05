from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Demonstrate abstraction
print(dog.make_sound()) 
print(cat.make_sound())  