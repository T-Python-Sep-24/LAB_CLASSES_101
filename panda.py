class Panda:
    def __init__(self,type:str,gender:str,age:int):
        self.type=type
        self.gender=gender
        self.age=age

    def sleep(self):
        print(f"panda{self.gender} sleep 16 hours per"
             f" day at the age of"
              f" {self.age}")

    def live(self):
        print(f"Panda{self.type} live almost 30yesr "
             f"and the oldest panda is {self.age}")