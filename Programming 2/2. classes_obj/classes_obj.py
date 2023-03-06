class Human:

    alive = True

    def speak(self):
        print("Humans are capable of speaking")
    
    def strength(self):
        print("Humans have strength")

human = Human()

print(human.alive), human.strength(), human.speak()