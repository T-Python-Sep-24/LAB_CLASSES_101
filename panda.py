class Panda:
    def __init__(self , name , age , major , GPA):
        self.name=name #atrribute
        self.age=age
        self.major=major
        self.GPA=GPA
        #method
    def interduce(self):
        return f"Hello , I'm {self.name}, I'm {self.age} years old"
    #method
    def dr(self):
        return f"my major is {self.major} , my GPA is {self.GPA}"
        
        
        