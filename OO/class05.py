# multiple inheritance
class Eletronic:

    def __init__(self, name):
        self._name = name
        self._on = False

    def turn_on(self):
        if not self._on:
            self._on = True
    
    def turn_off(self):
        if self._on:
            self._on = False

class MyPrinter():

    def my_printer(self, msg):
        print(msg)

class Smartphone(Eletronic, MyPrinter):

    def __ini__(self, name):
        super.__init__(name)

s1 = Smartphone("Samsung")
s1.turn_on()
s1.my_printer(s1._name)