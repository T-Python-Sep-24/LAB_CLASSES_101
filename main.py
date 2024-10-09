import definition

panda1= definition.Panda("Giant Panda","Ursidae","Central China","bamboo")
panda2= definition.Panda("Red Panda","Ailuridae","Eastern Himalayas","bamboo and fruits")
panda3= definition.Panda("Qinling Panda","Ursidae","Qinling Mountains","bamboo")
panda4= definition.Panda("Sichuan Giant Panda","Ursidae","China","bamboo")

print("attribute value: "+panda1.scientific_name)

print(panda1.basic_information())
print(panda1.is_bear())
print()
print(panda2.basic_information())
print(panda2.is_bear())
print()
print(panda3.basic_information())
print(panda3.is_bear())
print()
print(panda4.basic_information())
print(panda4.is_bear())
print()
      