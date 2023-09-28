
"""
Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0

Please observe the same placement of spaces and indentation.
"""


class CodeElement:
    indent_size = 2

    def __init__(self, name='', value=''):
        self.name = name
        self.value = value
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(i + 'class ' + self.name + ':')

        if not self.elements:
            i2 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(i2 + 'pass')
        else:
            i = ' ' * ((indent + 1) * self.indent_size)
            lines.append(i + 'def __init__(self):')

            for e in self.elements:
                i2 = ' ' * ((indent + 2) * self.indent_size)
                lines.append(i2 + 'self.' + e.name + ' = ' + str(e.value))

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = CodeElement(name=root_name)

    def add_field(self, type, name):
        self.__root.elements.append(
            CodeElement(type, name)
        )
        return self

    def __str__(self):
        return str(self.__root)


cb = CodeBuilder('Person')
print(cb)
