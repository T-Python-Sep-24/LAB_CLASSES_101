class Panda:
    def __init__(self, gender: str, age: int, weight: float, species: str) -> None:
       #4 Attributes 
        self.gender = gender        
        self.age = age  
        self.weight = weight         
        self.species = species    

    #  2 Methods
    def definition_of_species(self):
        species_definition = (
            f"The gender of this panda bear is: {self.gender}, "
            f"its age is {self.age}, its weight is about {self.weight} kg, "
            f"and it belongs to the species {self.species}."
        )
        return species_definition


    def fact(self):
        activities_of_life = (
            f"The weight of male pandas, {self.weight} kg, "
            f"is typically greater than that of females."
        )
        return activities_of_life
    
    