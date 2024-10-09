class Panda:
    def __init__(self, weight:float, height:float, gender:str, age:int, activity:str, favorite_food:str) -> None:
        """
        this is the constructor of the panda class initialization
        """
        # Panda attributes
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.activity = activity
        self.favorite_food = favorite_food

    # panda methods
    def metabolic_rate(self) -> float:
        """
        this function calculate bmr of a panda
        :return: bmr: float
        """
        bmr = 0
        if self.gender.lower() == "male":
            bmr: float = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.gender.lower() == "female":
            bmr: float = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        return bmr

    def daily_food_intake(self, bmr: float):
        """
        this function calculate food calories required in daily basses
        :param bmr:
        :return: cal: float
        """
        cal = 0
        if self.activity.lower() == "sedentary":
            cal = bmr * 1.2
            return cal
        elif self.activity.lower() == "light":
            cal = bmr * 1.375
            return cal
        elif self.activity.lower() == "moderate":
            cal = bmr * 1.55
            return cal
        elif self.activity.lower() == "very":
            cal = bmr * 1.725
            return cal
        elif self.activity.lower() == "super":
            cal = bmr * 1.9
            return cal


    def favFoodAmount(self, calories):
        """
        this function calculates the total grams required of the bandas favorite food calories per 100 grams
        :param calories:
        :return: grams: float
        """
        if self.favorite_food.lower() == "bamboo":
            grams = (calories / 75) * 100
            return grams
        elif self.favorite_food.lower() == "apples":
            grams = (calories / 52) * 100
            return grams
        elif self.favorite_food.lower() == "carrots":
            grams = (calories / 41) * 100
            return grams
        elif self.favorite_food.lower() == "watermelons":
            grams = (calories / 30) * 100
            return grams
        elif self.favorite_food.lower() == "Sweet Potatoes":
            grams = (calories / 86) * 100
            return grams