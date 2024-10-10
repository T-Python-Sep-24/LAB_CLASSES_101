class Panda:
    def __init__(self, name, age, weight, address):
        self.name =name 
        self.age = age 
        self.weight = weight 
        self.address = address

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"