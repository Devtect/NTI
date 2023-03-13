class Car:  # Creating a class called Car
    boost_amt = 200

    # Creating properties for the class called Car
    def __init__(self, brand, color, horsepower):
        self.brand = brand  # Creating the property named brand of the car
        self.color = color  # Creating the property named color of the car
        self.horsepower = horsepower  # Creating the property named horsepower of the car

    def __str__(self):
        return f"Brand: {self.brand} Color: {self.color} HP: {self.horsepower} Max Speed: {self.max_speed}"
    
    def boost(self):
        self.horsepower = self.horsepower + self.boost_amt
        return f"{self.brand} has been boosted!"

class Superbike(Car):
    boost_amt = 300
    def __init__(self, brand, color, horsepower, max_speed):
        super().__init__(brand, color, horsepower)
        self.max_speed = max_speed

vehicle1 = Superbike("BMW", "Black", 500, 280)  # Creating the 1st car with properties
vehicle2 = Superbike("Lexus", "Blue", 650, 310)

print(vehicle1)
print(vehicle2)
# print(vehicle1.boost())
# print(vehicle1)

