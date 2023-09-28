"""
Visitor Pattern.

It allows adding extra behavior to entire hierarchies of classes.

Visitor - a component (visitor) that knows how
to traverse a data structure composed
of (possibly related) types.

We jump into classes that are already been written
and modify them. Intrusive approach.
"""
# THIS APPROACH VIOLATES OCP!
# no general visitor solution here.
# buffer maybe can be taken as a visitor.


class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


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
    print(''.join(buffer), ' = ', e.eval())
