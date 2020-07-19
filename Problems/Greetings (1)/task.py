class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am " + self.name + "!")

name = input()

person = Person(name)
person.greet()
