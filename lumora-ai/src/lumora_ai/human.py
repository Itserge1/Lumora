import json
from dataclasses import dataclass

@dataclass
class HumanData:
    """Just the data structure"""
    name: str
    height: int
    weight: int

class Human:
    """The actual class with behavior"""
    # CLASS ATTRIBUTE - shared by all humans
    species = "Homo sapiens"

    def __init__(self, data: HumanData):
        # INSTANCE ATTRIBUTES - unique to each person
        self.name = data.name
        self.height = data.height
        self.weight = data.weight

    # Dunder methods to print instance infos
    def __str__(self):
        return f"{self.name} is {self.height}cm tall and weighs {self.weight}kg"

    # Instance method - accesses instance attributes
    def to_json(self):
        return json.dumps(self.__dict__)

    # Instance method - accesses instance attributes
    def get_name(self):
        return self.name  # Each person has their own name


    # Class method - accesses class attributes
    @classmethod
    def get_species(cls):
        return cls.species  # All humans share the same species

    @staticmethod
    def is_valid_human(my_spices):
        return my_spices.lower() == "homo sapiens"



# TESTING
if __name__ == "__main__":
    person1 = Human("Alice", 165, 60)
    person2 = Human("Bob", 180, 75)

    # print(person1.__str__()) # get instance information
    # print(person2.__str__()) # get instance information

    # print(person1.to_json())  # get instance information in json
    # print(person2.to_json())  # get instance information in json

    print(person1.get_name())  # Alice (unique to person1)
    print(person2.get_name())  # Bob (unique to person2)

    print(person1.get_species())  # Homo sapiens (same for all)
    print(person2.get_species())  # Homo sapiens (same for all)
    print(Human.get_species())  # Homo sapiens (can call on class itself)