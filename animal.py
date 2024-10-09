class panda:
    def __init__(self,name:str,height:float,gender:str,age:int) -> None:
        self.name=name
        self.height=height
        self.gender=gender
        self.age=age

    def get_panda(self)->str:
      
        panda=f"{self.name} is a {self.gender} panda! "
        return panda
    def get_information(self)->str:
        panda_informations=f"{self.name} is a {self.age} years old and it's {self.height}m long"
        return panda_informations
