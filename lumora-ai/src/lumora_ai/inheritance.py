# @abstractmethod
# @property

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some sound"

    def get_info(self):
        return f"{self.name} is {self.age} years old"


class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Override parent method
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print(dog.get_info())  # Buddy is 3 years old (inherited method)
print(dog.speak())  # Woof! (overridden method)
print(cat.speak())  # Meow!