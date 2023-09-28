"""
Memento Pattern.

Keep a memento of an object's state to return to that state.

Memento - a token/handle representing the system state.
Lets us roll back to the state when the token
was generated. May or may not directly expose
state information.


Whenever you have a change in the system, you can return a token
which gives you a snapshot of a current state.
So subsequently you can restore system back to the state
contained in the snapshot.
"""


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        # PROBLEM: we dont have a memento for initial state!
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        """Roll back the state of the system"""
        self.balance = memento.balance

    def __str__(self):
        return f'Balance = {self.balance}'


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    # restore to m1
    ba.restore(m1)
    print(ba)

    # restore to m2
    ba.restore(m2)
    print(ba)
