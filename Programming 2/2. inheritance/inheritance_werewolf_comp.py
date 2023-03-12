# Inheritance allows to use the properties and methods of one class in another

# general class human (parent class)
class Human:
    def __init__(self, speak):
        self.speak = speak
        
# general class wolf (parent class)   
class Wolf:
    def __init__(self, strength):
        self.strength = strength
             
# sub class werewolf (child class)
class Werewolf(Human, Wolf):
    def __init__(self, speak, strength, fur):
        super().__init__(speak)
        Wolf.__init__(self, strength)
        self.fur = fur
       

human = Human("Hello")
wolf = Wolf(10)
werewolf =  Werewolf("Howl", 50, "Brown")

print(human.speak)
print(wolf.strength)
print(werewolf.speak, werewolf.strength, werewolf.fur)