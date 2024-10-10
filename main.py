# main.py

from girl import Girl

# Meet 4 new friends!
girls = [
    Girl("Bayan", 23, "drawing", "lavender"),
    Girl("Rima", 21, "singing", "sky blue"),
    Girl("Wijdan", 24, "writing stories", "rose gold"),
    Girl("Sara", 22, "skateboarding", "mint green")
]

# Print each girl's name and let her introduce herself and share her favorite color
for girl in girls:
    print(f"Meet {girl.name}!")
    girl.introduce()
    girl.share_favorite_color()
