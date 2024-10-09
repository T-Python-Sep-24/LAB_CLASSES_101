class Panda:
    def __init__(self, name, age, weight, favorite_food):
        self.name = name
        self.age = age
        self.weight = weight
        self.favorite_food = favorite_food

    # Panda introduction Method
    def introduce(self):
        return f"Hi, I'm {self.name}. I'm {self.age} years old and weigh {self.weight} kg."

    # Panda's favorite food Method
    def eat(self):
        return f"{self.name} loves eating {self.favorite_food}!"