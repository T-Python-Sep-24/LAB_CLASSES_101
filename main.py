from pandaClass import Panda 


def main():
    panda1 = Panda("Giant Panda", "White & black", 91, "China", 1850)
    panda2 = Panda("Red Panda", "Red & black", 5, "Nepal", 10000)
    panda3 = Panda("Qinling Panda", "White & Brown", 5, "China", 100)
    panda4 = Panda("fossil panda","unknown",150,"China",0)

    print(panda2.species)
    print(panda2.fur)
    print(panda2.weight)
    print(panda2.found)

    for panda in [panda1,panda2,panda3,panda4]:
        panda.taypPanda()
        panda.extinction()
        print("\n")

main()
