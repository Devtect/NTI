class Car:  # Creating a class called Car
    # Creating properties for the class called Car
    def __init__(self, brand, color, horsepower):
        self.brand = brand  # Creating the property named brand of the car
        self.color = color  # Creating the property named color of the car
        self.horsepower = horsepower  # Creating the property named horsepower of the car

    def __str__(self):
        return f"Brand: {self.brand} Color: {self.color} HP: {self.horsepower}"
    
    def boost(self):
        self.horsepower += 200
        return f"{self.brand} has been boosted to {self.horsepower} horsepower!"

car1 = Car("BMW", "Black", 500)  # Creating the 1st car with properties
car2 = Car("Lexus", "Blue", 650)

print(car1)
print("Brand:", car1.brand +" "+"Color:", car1.color +" "+"HP:", car1.horsepower)
print(car1.boost())
