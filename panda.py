class Panda:
    def __init__(self, name, age, color, sleepAvg):
        self.name = name
        self.age = age
        self.color = color
        self.sleepAvg = sleepAvg

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} sleeps average of {self.sleepAvg} hours."
