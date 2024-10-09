from panda import Panda

# creating 4 instances
panda1 = Panda("Cz", "male", 110)
panda2 = Panda("Sarah", "female", 120, 2)
panda3 = Panda("Fj", "male", 270, 5)
panda4 = Panda("Tooti", "female", 115)

# printing an attribute
print(f"panda name: {panda1.name}")

# Call the two methods on the instances
print(panda1.showInfo())
print(f"new weight: {panda1.eatFood(3):.2f}\n")

print(panda2.showInfo())
print(f"new weight: {panda2.eatFood(4):.2f}\n")

print(panda3.showInfo())
print(f"new weight: {panda3.eatFood(12):.2f}\n")

print(panda4.showInfo())
print(f"new weight: {panda4.eatFood(6):.2f}\n")
