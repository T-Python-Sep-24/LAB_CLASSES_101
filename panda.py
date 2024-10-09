class Panda:
    def __init__(self , name , age , live, fvFood):
        self.name=name #atrribute
        self.age=age
        self.live=live
        self.fvFood=fvFood
        #method
    def interduce(self):
        return f"Hello , The panda {self.name}, a {self.age} year old panda"
    #method
    def dr(self):
        return f"loves eating {self.fvFood} , live in {self.live}"
        
        
        