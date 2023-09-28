"""
Singleton Coding Exercise
Since implementing a singleton is easy,
you have a different challenge:
write a function called is_singleton() .
This method takes a factory method that
returns an object and it's up to you
to determine whether or not that object
is a singleton instance.
"""


def is_singleton(factory):
    obj1 = factory()
    obj2 = factory()
    return obj1 is obj2


if __name__ == '__main__':
    def factory_method():
        return [1, 2, 3]

    print(is_singleton(factory_method))  # Output: False

    def singleton_factory():
        return "Singleton"

    print(is_singleton(singleton_factory))  # Output: True
