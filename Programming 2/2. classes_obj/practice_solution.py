class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    # def get_house(self):
    #    return f"The house is colored {self.color} and has {self.rooms} rooms"


house1 = House("Pink", 5)

print(house1.color)
print(house1.rooms)
# print(house1.get_house())