"""
Command Coding Exercise
Implement the Account.process()
method to process different account commands.

The rules are obvious:

success indicates whether the operation was successful

You can only withdraw money if you have enough in your account
"""

from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW:
            if self.balance >= command.amount:
                self.balance -= command.amount
                command.success = True
            else:
                command.success = False
        else:
            raise ValueError("Invalid action in command")


# Test case
def test_account_processing():
    account = Account(balance=100)

    command1 = Command(Command.Action.DEPOSIT, 50)
    account.process(command1)
    assert account.balance == 150
    assert command1.success is True

    command2 = Command(Command.Action.WITHDRAW, 75)
    account.process(command2)
    assert account.balance == 75
    assert command2.success is True

    command3 = Command(Command.Action.WITHDRAW, 100)
    account.process(command3)
    assert account.balance == 75
    assert command3.success is False

    command4 = Command(Command.Action.DEPOSIT, 25)
    account.process(command4)
    assert account.balance == 100
    assert command4.success is True

    command5 = Command(Command.Action.WITHDRAW, 100)
    account.process(command5)
    assert account.balance == 0
    assert command5.success is True

    command6 = Command(Command.Action.WITHDRAW, 10)
    account.process(command6)
    assert account.balance == 0
    assert command6.success is False


if __name__ == "__main__":
    test_account_processing()