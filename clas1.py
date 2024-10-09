class Panda:
    def __init__(self,age,weight,height,number):
        self.age=age
        self.weight=weight
        self.height=height
        self.number=number


    def get_info(self):
        print(f"Panda age: {self.age} years, Weight: {self.weight} kg, "
                f"Height: {self.height} cm, Number: {self.number}")

    def playing(self,timing):
        self.timing=timing
        print(f"panda number {self.number} is playing for {self.timing} min")