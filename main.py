from definitionClass import Panda

# Create instances of the Panda class
animal_panda_1 = Panda("BOBO", 12, 250.0, "funny", "Chengdu, China")
animal_panda_2 = Panda("Poki", 5, 300.0, "Sick", "Moscow, Russia")
animal_panda_3 = Panda("Tao", 12, 250.0, "Playful", "JKyoto, Japan")
animal_panda_4 = Panda("Zuri", 12, 250.0, "angry", "Riyadh, saudi arabia")

# Display and print the panda's information
print(animal_panda_1.display_information())
print(animal_panda_1.status)

print(animal_panda_2.display_information())
print(animal_panda_2.name)

print(animal_panda_3.display_information())
print(animal_panda_3.age)

print(animal_panda_4.display_information())
print(animal_panda_4.live)