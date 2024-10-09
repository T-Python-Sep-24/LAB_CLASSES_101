#Lab 12

class Panda:

    #First you initilize the class
    def __init__(self, species: str, name:str, gender:str, age:int, habitat:str, health_status:str) -> None:
        #Attributes
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age
        self.habitat = habitat
        self.health_status = health_status


    #Methods    
    def Panda_Zoo(self):
        introduction = f"Hi my Name is '{self.name}', and I am a {self.gender}. And I am {self.age} years old"
        print(introduction)
        return introduction
    

    def is_adult(self):
        """Checks if the panda is an adult based on its age."""
        if self.age >= 5:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is still young.")


    def update_health_status(self, new_status: str):
        self.health_status = new_status
        print(f"{self.name}'s health status is now {self.health_status}.")


'''
A small test befor I move it to the main file
#instances/objects

Panda1 = Panda("Red Panda", "Ruby", "Female", 6, "Temperate forests in the eastern Himalayas, including Nepal, Bhutan, and China", "Healthy")
Panda1.Panda_Zoo()
Panda1.is_adult()
Panda1.update_health_status("A little under the weather (A small fever)")

Panda2 = Panda("Brown Pandas", "Teddy", "Male", 12, "High-altitude bamboo forests in the Qinling Mountains, Shaanxi Province.", "Healthy")
Panda2.Panda_Zoo()
Panda2.is_adult()
Panda2.update_health_status("Not Healthy")

Panda3 = Panda("Giant Pandas", "Bao", "Female", 10, "Bamboo forests in mountainous regions of central China", "Sick")  
Panda3.Panda_Zoo()
Panda3.is_adult()
Panda3.update_health_status("Healthy")

Panda4 = Panda("Qinling Panda", "Q", "Male", 2, "Qinling Mountains in Shaanxi Province, China, with dense bamboo forests", "Stomach Ache")
Panda4.Panda_Zoo()
Panda4.is_adult()
Panda4.update_health_status("Healthy")       



print(Panda1.habitat)
print(Panda2.health_status)

'''