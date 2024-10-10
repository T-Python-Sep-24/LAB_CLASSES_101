from panda import Panda 

Girl1= Panda("Reema", 23, 52, "Riyadh")
Girl2= Panda("Nouf", 27, 60, "Khobar")
Girl3= Panda("Reema", 23, 52, "Dammam")
Girl4= Panda("Reema", 23, 52, "Dammam")

for panda in [Girl1, Girl2, Girl3, Girl4]:
    print(f"Name:{panda.name}")
    print(panda.eat())
    print(panda.sleep())
    print()