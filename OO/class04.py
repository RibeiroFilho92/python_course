# inheritance
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
class Client(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
