"""
Prototype Factory Pattern

If you have few predefined prototypes in your app,
it would be nice to package them into a factory.
And provide factory methods so that nobody has to just take a prototype
and perform a deep copy and perform customization by hand.
It is much easier to wrap it into a separate component.

"""
import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.street_address = street_address
        self.city = city

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Drive', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Drive', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


john = EmployeeFactory.new_main_office_employee('John', 101)
jane = EmployeeFactory.new_aux_office_employee('Jane', 501)

print(john)
print(jane)
