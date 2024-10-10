from panda import Panda

def main():
    panda1 = Panda("Po", 1.5, 100, "China")
    panda2 = Panda("Tao", 1.3, 90, "China")
    panda3 = Panda("Ling", 1.2, 85, "Japan")
    panda4 = Panda("Xiao", 1.4, 95, "South Korea")

    print(f"Panda 1: {panda1.name}, Height: {panda1.height}m")
    panda1.eat()
    panda1.show_stats()

    print(f"Panda 2: {panda2.name}, Height: {panda2.height}m")
    panda2.eat()
    panda2.show_stats()

    print(f"Panda 3: {panda3.name}, Height: {panda3.height}m")
    panda3.eat()
    panda3.show_stats()

    print(f"Panda 4: {panda4.name}, Height: {panda4.height}m")
    panda4.eat()
    panda4.show_stats()

if __name__ == "__main__":
    main()
