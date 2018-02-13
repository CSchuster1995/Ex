class Animal:
    def __init__ (self, name):
        self.name = name

class Dog (Animal):
    def woof (self):
        print("woof")

class ShihTzu (Dog):
  def woof (self):
    print("Yip Yip")

class Cat (Animal):
    def meow (self):
        print("Meow)")