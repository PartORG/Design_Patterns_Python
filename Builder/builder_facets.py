"""
Complication of a Builder Pattern.

How you can get several builders
participating in building up an object.

How to make a nice interface
to jump from one Builder to another.

This approach violates an Open-Close Principle
"""


class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}' +\
            f'Employed at {self.company_name} as a {self.position} earning {self.income}'


class PersonBuilder:
    """Fluent interface that jumps from one Builder to another"""

    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()
person = pb\
    .lives\
        .at('123 London Road')\
        .in_city('London')\
        .with_postcode('SW12BC')\
    .works\
        .at('Fabrikam')\
        .as_a('Engineer')\
        .earning(123000)\
    .build()

print(person)
