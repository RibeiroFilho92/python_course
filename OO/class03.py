class Car:

    def __init__(self, name):
        self.name = name
        self.engine = None
        self.manufacture = None

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name
    
    @property
    def engine(self):
        return self.engine
    
    @engine.setter
    def engine(self, engine):
        self.engine = engine

    @property
    def manufacture(self):
        return self.manufacture
    
    @manufacture.setter
    def manufacture(self, manufacture):
        self.manufacture = manufacture

class Engine:

    def __init__(self, name):
        self.name = name
        self.cars = []
        self.manufacture = None

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name

class Manufacture:

    def __init__(self, name):
        self.name = name
        self.cars = []