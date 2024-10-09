class Panda:
    def __init__(self, name: str , age : int , weight : float , status : str ,  live : str  ) -> None:
        self.name = name
        self.age = age 
        self.weight = weight 
        self.status = status 
        self.live = live 


    def display_information(self):
        return  f"Panda Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Status: {self.status}, Lives in: {self.live}" 
    