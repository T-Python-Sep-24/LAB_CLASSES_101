
class Panda:
    
    def __init__(self, weight:float, height:float, age:int, color:str):
        self.weight = weight
        self.height = height
        self.age = age
        self.color = color
    
    def get_mass(self):
        print(round(self.weight / self.height, 2))
    
    def display_info(self):
        print(f'weight: {self.weight}, height: {self.height}, age: {self.age}, color: {self.color}')
    
    
        