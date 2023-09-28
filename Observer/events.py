"""
Observer Pattern

Observer - is an object that wishes to be informed about
events happening in the system. The entity generating
the events is an Observable.


Notifications on events example
"""


class Event(list):
    """List of functions which need to be invoked
    whenever this event happens """
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        """Use event and call it."""
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    """ doctor needs to be notified"""
    print(f'{name} needs a doctor at {address}')


if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker Str.')
    person.falls_ill.append(
        lambda name, address: print(f'{name} is ill.')
    )
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()

    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
