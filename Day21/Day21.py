# Day 21

# Class Inheritence - This concept is used if we want one class to have/inherit attributes and methods of another class
# Syntax - class class2(class1):
                #def __init__(self):
                    # super().__init__()

"Example"

class Animal:
    def __init__(self):
        self.no_of_eyes=2
    def breathe(self):
        print("Inhale and exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("Under the water.")

    def swim(self):
        print("Swims in water")


nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.no_of_eyes)


