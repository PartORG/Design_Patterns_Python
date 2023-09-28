"""
Visitor Pattern.

It allows adding extra behavior to entire hierarchies of classes.

Reflective Visitor Example
"""
from abc import ABC

# ADVANTAGE:
# all printing stuf is in a separate class


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


if __name__ == '__main__':
    # 1 + (2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []
    e.print(buffer)

    # ExpressionPrinter.print(e, buffer)

    print(''.join(buffer))
