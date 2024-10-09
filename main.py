import panda_file

#create objects of pandas
panda1 = panda_file.Panda("Sticky Bun", 5, "Giant Panda", 120)
panda2 = panda_file.Panda("Sugar Cookie", 3, "Red Panda", 100)
panda3 = panda_file.Panda("Sugar Plum", 7, "Red Panda", 130)
panda4 = panda_file.Panda("Sunshine", 4, "Giant Panda", 110)



print(f"\nName of Panda 1: {panda1.name}")  #print 1 attribute value
print(panda1.introduce())    #method 1
panda1.eat(50)    #method 2
print(panda1.introduce()) 

print(f"\nName of Panda 2: {panda2.name}")
print(panda2.introduce())  
panda2.eat(50)  
print(panda2.introduce())  


print(f"\nPanda 3 is: {panda3.species}")
print(panda3.introduce())  
panda3.eat(50) 
print(panda3.introduce())  

print(f"\nPanda 4 is: {panda4.species}")
print(panda4.introduce())  
panda4.eat(50)
print(panda4.introduce())  
