class Panda:

    def __init__(self, name, height, weight, country_of_origin):
        self.name = name
        self.height = height
        self.weight = weight
        self.country_of_origin = country_of_origin

    def eat(self):
        print(f"{self.name}, a panda from {self.country_of_origin}, is eating.")


    def show_stats(self):
        print(f"{self.name} is {self.height} meters tall and weighs {self.weight} kg.")
