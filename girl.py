# girl.py

class Girl:
    def __init__(self, name, age, hobby, favorite_color):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.favorite_color = favorite_color
 
    def introduce(self):
        print(f"Hey, I’m {self.name}. I’m {self.age} years old and I love {self.hobby}!")

    def share_favorite_color(self):
        print(f"My favorite color is {self.favorite_color}, it’s so pretty!")
