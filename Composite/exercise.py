"""
Composite Coding Exercise
Consider the code presented below.
We have two classes called SingleValue and ManyValues.
SingleValue stores just one numeric value,
but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property
member called sum that returns a sum of all the values
that the object contains. Please ensure that there is only
a single method that realizes the property sum, not multiple methods.

Here is a sample unit test:

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)
"""
import unittest

from abc import ABC, abstractmethod


class Value(ABC):
    @abstractmethod
    def sum(self):
        pass


class SingleValue(Value):
    def __init__(self, value):
        self.value = value

    @property
    def sum(self):
        return self.value


class ManyValues(Value):
    def __init__(self):
        self.values = []

    def append(self, value):
        self.values.append(value)

    @property
    def sum(self):
        total = 0
        for value in self.values:
            if isinstance(value, Value):
                total += value.sum
            else:
                total += value
        return total


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)


if __name__ == '__main__':
    print('Solution')
