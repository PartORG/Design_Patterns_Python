"""
Decorator Pattern.
Python Functional Decorator.


Adding behavior without altering the class itself.
Facilitates the addition of behaviors to individual
objects without inheriting from them.
"""
import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int((end-start)*1000)}ms')
        return result
    return wrapper


# python decorator
@time_it
def some_op():
    print('Starting the operation')
    time.sleep(1)
    print('We are done')
    return 123


if __name__ == '__main__':
    # some_op()
    # time_it(some_op)()
    some_op()
