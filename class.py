class Computer:
    def config(self):
        print("I7, 16GB, 1TB");

com1 = Computer()

Computer.config(com1)
print("What?")
com1.config()
