"""
Factory Coding Exercise
You are given a class called 'Person' .
The person has two attributes: 'id' , and 'name' .

Please implement a  'PersonFactory' that has a non-static
'create_person()'  method that takes a person's name and
return a person initialized with this name and an id.

The 'id' of the person should be set as a 0-based index
of the object created.
So, the first person the factory makes
should have Id=0, second Id=1 and so on.
"""


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    def __init__(self):
        self.index = 0

    def create_person(self, name):
        person = Person(self.index, name)
        self.index += 1
        return person


if __name__ == '__main__':
    print('Solution:')

    factory = PersonFactory()

    person1 = factory.create_person("John")
    print(person1.id)  # Output: 0
    print(person1.name)  # Output: John

    person2 = factory.create_person("Alice")
    print(person2.id)  # Output: 1
    print(person2.name)  # Output: Alice

    person3 = factory.create_person("Bob")
    print(person3.id)  # Output: 2
    print(person3.name)  # Output: Bob
