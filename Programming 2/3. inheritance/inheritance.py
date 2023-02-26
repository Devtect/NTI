# Inheritance allows to use the properties and methods of one class in another

# general class human (parent class)
class human:
    def __init__(self, brain):
        self.brain = brain
    
    

class person(human):
    def __init__(self, brain):
        super().__init__(brain)

    def name(self, name):
        print(f"My name is {self.name}!")