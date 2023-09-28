"""
Interface Segregation Principle
You do not want to stick too many elements (methods) into an Interface.
IDEA:
    Instead of having one large interface with several members in it,
    you want to keep things granular, you want to split this interface
    into several parts that  people can implement.
"""

from abc import abstractmethod

# Interface
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):

    def print(self, document):
        # OK
        pass

    def fax(self, document):
        # it can not fax
        pass  # no operation

    def scan(self, document):
        # it can not scan
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


# FIXING:
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


# then
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


# or
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
