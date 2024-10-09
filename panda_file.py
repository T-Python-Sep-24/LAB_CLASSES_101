class Panda:

    
    def __init__(self, name:str, age:int, species:str,  weight:int) :
        #addtributes/ properties
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    
    #methods
    def introduce(self):
        introduction = f"Panda name is {self.name} , of Species {self.species} and its age is {self.age} years old with weight of {self.weight} kg"
        return introduction
    
    
    def eat(self, food):
        self.weight += food * 0.1

