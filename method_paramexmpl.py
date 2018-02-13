class Person:
    def __init__ (self,name):
        self.name = name

    def greet(self, friend):
        print("Hello {} and {}" .formant(self.name, friend))

me = Person('Connor')
me.greet('Bob')