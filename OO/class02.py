# _protected __private
class Person:

    def __init__(self, name, surname, age):
        self._name =  name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._namename
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, surname):
        self._surname = surname
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age