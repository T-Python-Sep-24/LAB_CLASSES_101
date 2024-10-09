from Classes import Panda

panda1 = Panda(80, 1.1, 7, 'white') 
panda2 = Panda(500, 1.2, 15, 'black') 
panda3 = Panda(100, 1.5, 15, 'white_black') 
panda4 = Panda(800, 1.8, 20, 'white_brown') 

print('height:', panda4.height)

print('\nThe Masses')
panda1.get_mass()
panda2.get_mass()
panda3.get_mass()
panda4.get_mass()

print('-'*50)

print('\nThe Info')
panda1.display_info()
panda2.display_info()
panda3.display_info()
panda4.display_info()