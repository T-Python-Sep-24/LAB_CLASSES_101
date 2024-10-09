# definition the class Panda
class Panda:

    def __init__(self,scientific_name:str,family:str,location:str,food:str) -> None:
        self.scientific_name=scientific_name
        self.family=family
        self.location=location
        self.food=food
    def  basic_information(self):
        info=f"The panda scientific name is {self.scientific_name}, from {self.family} family, This type of panda eats {self.food} and lives in {self.location}"
        return info
    def is_bear(self):
        result=f"It is not from bear family"
        if self.family.lower() == "ursidae" or self.family.lower() =="bear":
            result=f"It is from bears family"
            return result
        return result
