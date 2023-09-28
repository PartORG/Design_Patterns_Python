"""
Mediator Pattern.

This pattern facilitates communication between components.

Mediator - a component that facilitates communication between
other components without them necessarily being aware of
each other or having direct (reference) access to each other.

Chat Room Example.
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def private_message(self, who, message):
        # central mediator
        self.room.message(self.name, who, message)

    def say(self, message):
        self.room.broadcast(self.name, message)


class ChatRoom:
    """Used as a Mediator"""
    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == '__main__':
    room = ChatRoom()
    john = Person('John')
    jane = Person('Jane')

    room.join(john)
    room.join(jane)

    john.say('hi room!')
    john.say('oh, hey John')

    simon = Person('Simon')
    room.join(simon)
    simon.say('Hi everyone!')

    jane.private_message('Simon', 'glad you could join')
