class Human:
    def speak(self):
        print("can speak")

class Wolf:
    def strength(self):
        print("very strong")

class Werewolf(Human, Wolf):
    pass

human = Human()
wolf = Wolf()
werewolf = Werewolf()



werewolf.speak()
werewolf.strength()

