class Person:

    def __init__(self, name, surname):
        self.name =  name
        self.surname = surname

    def who_I_am(self):
        return f"Hello, I'm {self.name} {self.surname}"

p1 = Person("Ribeiro", "Filho")
print(p1.who_I_am())