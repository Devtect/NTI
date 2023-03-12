class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
class Developer(Employee):
    def __init__(self, name, age, prog_lang):
        super().__init__(name, age)
        self.prog_lang = prog_lang

    def get_lang(self):
        return self.prog_lang
    
employee1 = Developer("Jason Bourne", 34, "C#")

print(employee1.get_age())
print(employee1.get_name())
print(employee1.get_lang())