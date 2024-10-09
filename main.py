#Creating Panda class
class Panda:

    def __init__(self, name: str ,age: int, gender: str, weight: int, diet: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.diet = diet
    
    def info(self) -> str:
        '''
        This method prints information of a specific panda
        '''
        information:str = f"Panda info:\nName: {self.name}\nAge: {self.age} years old.\nGender: {self.gender}\nWeight: {self.weight}kg.\nWhat it usually eats: {self.diet}"
        return information
    
    def changeWeight(self, newWeight: int) -> str:
        '''
        This method changes the weight of the panda
        '''
        self.weight = newWeight
        return f"Weight has been changed to: {self.weight}kg."
    
#Main program
panda1 = Panda("Zezo", 200, "Male", 350, "Bamboo")
panda2 = Panda("Lora", 150, "Female", 200, "Fish")
panda3 = Panda("Ibra", 320, "Male", 400, "Bamboo - Eggs")
panda4 = Panda("Jojo", 120, "Female", 210, "Bamboo - Ground meat")

#Operations on instances

#Printing each panda's info first then changing the weight
print(f"First panda's name is {panda1.name}")
pandaInfo: str = panda1.info()
print(pandaInfo)
newWeight = panda1.changeWeight(250)
print(f"Weight after changing: {newWeight}Kg\n")

print(f"Second panda's age is {panda2.age}")
pandaInfo = panda2.info()
print(pandaInfo)
newWeight = panda1.changeWeight(165)
print(f"Weight after changing: {newWeight}Kg\n")

print(f"Third panda's gender is {panda3.gender}")
pandaInfo = panda3.info()
print(pandaInfo)
newWeight = panda1.changeWeight(333)
print(f"Weight after changing: {newWeight}Kg\n")

print(f"Fourth panda's diet is {panda4.diet}")
pandaInfo = panda4.info()
print(pandaInfo)
newWeight = panda1.changeWeight(144)
print(f"Weight after changing: {newWeight}Kg\n")
