from panda import Panda

def main():
    # Creating instances of the Panda class
    panda1 = Panda("male", 5, 100.0, "Ailuropoda melanoleuca")
    panda2 = Panda("female", 4, 90.0, "Ailuropoda melanoleuca")
    panda3 = Panda("male", 6, 110.0, "Ailuropoda melanoleuca")
    panda4 = Panda("female", 3, 85.0, "Ailuropoda melanoleuca")

 
    for panda in [panda1, panda2, panda3, panda4]:
        print(f"Panda Gender: {panda.gender}")
        print(panda.definition_of_species())
        print(panda.fact())
        print()  

if __name__ == "__main__":
    main()