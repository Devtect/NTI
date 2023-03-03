# In programming context polymorphism means that the same entity(method, operator, object) can have different forms(usage)


# Operator polymorphism '+'
# In the example below "+" operator used to perfrom two different operations.

# Adding two numbers
num1 = 4
num2 = 5
print(num1 + num2)
# String concatination 
str1 = "Jason "
str2 = "Bourne"
print(str1+str2)

#------------------------------------------------------------------------------------------------------

# Function polymorphism
print(len("Jason Bourne"))  # len() used to get the length of a string
print(len(["BMW", "Lexus", "Ferrari"])) # len() used to get the number of items in a list
print(len({"Name": "Jason Bourne", "Location": "Unknown"})) # len() used to get the number of keys

#------------------------------------------------------------------------------------------------------

# Class method polymorphism (Method overriding)

'''
In the example below, we used two different classes called Plane and Car. 
Notice that we used the same method called "size", even though classes
are not linked or has superclass
'''

class Plane:
    def __init__(self, name):
        self.name = name

    def size(self):          
        print(f"This is an {self.name}. And it's a BIG PLANE")

class Car:
    def __init__(self, name):
        self.name = name
    
    def size(self): 
        print(f"This is a {self.name}. And it's a SMALL CAR")

plane = Plane("Airbus 737")
car = Car("Nissan GTR")

for vehicle in (plane, car):
    vehicle.size()

#------------------------------------------------------------------------------------------------------

# Inheritance polymorphism (Method overriding)

class Vehicle:
    def engine(self):
        print("Vehicles have engines.")
    def size(self):
        print("Vehicles have different sizes.")
    

class Plane(Vehicle):
    def size(self):
        print("A plane is a BIG vehicle.")

class Car(Vehicle):
    def size(self):
        print("A car is a SMALL vehicle.")

vehicle = Vehicle()
plane = Plane()
car = Car()

vehicle.engine()
vehicle.size()

plane.engine()
plane.size()    

car.engine
car.size()    

#------------------------------------------------------------------------------------------------------

# Function overloading 
# Python does not support traditional function overloading 
# In the example below, we are using default arguments to achive function overloading

def calculate(x, y=None, z=None):
    if y is None and z is None:
        return x
    elif z is None:
        return x + y
    else:
        return x + y + z

print(calculate(2))           # Output: 2
print(calculate(2, 3))        # Output: 5
print(calculate(2, 3, 4))     # Output: 9

#------------------------------------------------------------------------------------------------------