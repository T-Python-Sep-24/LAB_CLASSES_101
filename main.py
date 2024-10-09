from panda import Panda

def app():

    weight = float(input("Enter Panda weight (kg): "))  # e.g., 100
    height = float(input("Enter Panda height (cm): "))  # e.g., 150
    gender = input("Enter Panda gender [male/female]: ")  # e.g., male
    age = int(input("Enter Panda age (years): "))  # e.g., 5
    activity = input("Enter Panda activity [sedentary/light/moderate/very/super]: ")  # e.g., moderate
    favorite_food = input("Enter Panda favorite food [bamboo/apples/carrots/watermelons]: ")  # e.g., bamboo

    # objects of the panda class
    panda1 = Panda(weight, height, gender, age, activity, favorite_food)
    panda2 = Panda(120, 150, "female", 7, "very", "watermelons")
    panda3 = Panda(90, 130, "female", 4, "super", "carrots")
    panda4 = Panda(190, 150, "female", 2, "moderate", "apples")

    # calling panda1 methods
    bmr = panda1.metabolic_rate()
    cal = panda1.daily_food_intake(bmr)
    grams = panda1.favFoodAmount(cal)

    # calling panda2 methods
    bmr2 = panda2.metabolic_rate()
    cal2 = panda2.daily_food_intake(bmr)
    grams2 = panda2.favFoodAmount(cal)

    bmr3 = panda2.metabolic_rate()
    cal3 = panda2.daily_food_intake(bmr)
    grams3 = panda2.favFoodAmount(cal)

    bmr4 = panda2.metabolic_rate()
    cal4 = panda2.daily_food_intake(bmr)
    grams4 = panda2.favFoodAmount(cal)

    # accessing panda attribute/property
    print(f"Panda 1: The amount of {panda1.favorite_food} needed: {grams:.2f} grams")
    print(f"Panda 2: The amount of {panda2.favorite_food} needed: {grams2:.2f} grams")
    print(f"Panda 3: The amount of {panda3.favorite_food} needed: {grams3:.2f} grams")
    print(f"Panda 4: The amount of {panda4.favorite_food} needed: {grams4:.2f} grams")

app()