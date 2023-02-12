from abc import ABC, abstractmethod

class MyPrinterAbs(ABC):

    @abstractmethod
    def my_printer(self, msg):
        ...

# m = MyPrinterAbs() TypeError!

class MyPrinter(MyPrinterAbs):

    def my_printer(self, msg):
        print(msg)

m = MyPrinter()
m.my_printer("Works")