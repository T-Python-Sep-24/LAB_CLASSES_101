#This is the main file where I will be calling the class

from Lab12 import Panda

#instances/objects

Panda1 = Panda("Red Panda", "Ruby", "Female", 6, "Temperate forests in the eastern Himalayas, including Nepal, Bhutan, and China", "Healthy")
Panda1.Panda_Zoo()
Panda1.is_adult()
Panda1.update_health_status("A little under the weather (A small fever)")

print("\n")

Panda2 = Panda("Brown Pandas", "Teddy", "Male", 12, "High-altitude bamboo forests in the Qinling Mountains, Shaanxi Province.", "Healthy")
Panda2.Panda_Zoo()
Panda2.is_adult()
Panda2.update_health_status("Not Healthy")

print("\n")

Panda3 = Panda("Giant Pandas", "Bao", "Female", 10, "Bamboo forests in mountainous regions of central China", "Sick")  
Panda3.Panda_Zoo()
Panda3.is_adult()
Panda3.update_health_status("Healthy")

print("\n")

Panda4 = Panda("Qinling Panda", "Q", "Male", 2, "Qinling Mountains in Shaanxi Province, China, with dense bamboo forests", "Stomach Ache")
Panda4.Panda_Zoo()
Panda4.is_adult()
Panda4.update_health_status("Healthy")       

print("\n")

print(Panda1.habitat)
print(Panda2.health_status)