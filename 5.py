class Parent():
    def print_lastname(self):
        print("Shaikh")

class Child(Parent):
    def print_firstname(self):
        print("Danish")

d = Child()
d.print_firstname()
d.print_lastname()
