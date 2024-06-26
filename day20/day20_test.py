class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()    # inherit attribute, method from super class
# The call to super() in the initialiser is recommended, but not strictly required.
    def breathe(self):
        super().breathe()    # from parent, can be deactivated
        print("doing this underwater.") # from self (new)
    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()     # method
print(nemo.num_eyes)     # attribute
nemo.breathe()