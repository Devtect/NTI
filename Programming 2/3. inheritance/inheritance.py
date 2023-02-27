# Inheritance allows to use the properties and methods of one class in another

# general class human (parent class)

class human:
    def __init__(self, speak):
        self.speak = speak

# general class wolf (parent class)   
class wolf:
    def __init__(self, strength):
        self.strength = strength
       
# sub class werewolf (child class)
class werewolf(human, wolf):
    def __init__(self, speak, strength):
        super().__init__(speak, strength)
       
    def __init__(self, fur):
        self.fur = fur