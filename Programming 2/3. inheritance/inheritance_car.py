class Car:  # Creating a class called Car
    boost_amt = 200

    # Creating properties for the class called Car
    def __init__(self, brand, color, horsepower):
        self.brand = brand  # Creating the property named brand of the car
        self.color = color  # Creating the property named color of the car
        self.horsepower = horsepower  # Creating the property named horsepower of the car

    def __str__(self):
        return f"Brand: {self.brand} Color: {self.color} HP: {self.horsepower}"
    
    def boost(self):
        self.horsepower = self.horsepower + self.boost_amt
        return f"{self.brand} has been boosted!"


vehicle1 = Car("BMW", "Black", 500)  # Creating the 1st car with properties
vehicle2 = Car("Lexus", "Blue", 650)

print(vehicle1)
print(vehicle1.boost())
print(vehicle1)

