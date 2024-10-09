class Panda:
    def __init__(self, name: str, gender: str, weight: float, age: int = 1) -> None:
        self.name = name
        self.gender = gender
        self.weight = weight
        self.age = age

    def showInfo(self) -> str:
        info: str = (f"name: {self.name},   gender: {self.gender},  " + 
                     f"weight: {self.weight},   age: {self.age}\n")
        return info

    def eatFood(self, foodInKG: float) -> float:
        print("Chommm! Chommm! Chommm!")
        self.weight += foodInKG / 3
        return self.weight 
