from panda import Panda

# Creating four instances of the Panda class
panda1 = Panda("Po", 5, 100, "bamboo")
panda2 = Panda("Ling", 3, 80, "apples")
panda3 = Panda("Mei", 7, 90, "carrots")
panda4 = Panda("Bao", 4, 85, "bamboo shoots")

# Printing 1 attribute value from each instance
print(panda1.name)  # output: Po
print(panda2.age)   # output: 3
print(panda3.weight)  # output: 90
print(panda4.favorite_food)  # output: bamboo shoots

# Calling the two methods on each instance
print(panda1.introduce())
print(panda1.eat())

print(panda2.introduce())
print(panda2.eat())

print(panda3.introduce())
print(panda3.eat())

print(panda4.introduce())
print(panda4.eat())
