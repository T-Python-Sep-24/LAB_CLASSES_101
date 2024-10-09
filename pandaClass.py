class Panda:

    def __init__(self, species:str, fur:str, weight:float,found: str ,number:int) -> None:

        self.species = species
        self.fur = fur
        self.found = found
        self.weight = weight
        self.number = number

    def taypPanda(self):

        describe = f"{self.species} - {self.fur} - {self.weight}KG - {self.found} "
        print(describe)
    
    def extinction(self):

        if self.number <= 2000 and self.number > 0:
           Extinct = f"{self.species}  endangered species"
           print(Extinct)
        elif self.number == 0:
             Extinct = f"{self.species} extinct"
             print(Extinct)
        else:
            print(f"{self.species} not endangered species")

   

  







