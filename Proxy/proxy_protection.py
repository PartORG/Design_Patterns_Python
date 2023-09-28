"""
Proxy Pattern.

Protection.

Proxy -- an interface for accessing a particular resource.
Proxy - a class that functions as an interface to a particular resource.
That resource may be remote, expensive to construct,
or may require logging or some other added functionality.
"""


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver.name}')


# Proxy
class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        #  Protection Proxy
        # additional functionality
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    driver = Driver('John', 10)
    car = CarProxy(driver)
    car.drive()
