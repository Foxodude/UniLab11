class Restaurant:
    def __init__(self, restaurantName, cuisineType, rating):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        if int(int(rating >5) or int(rating < 0)):
            print("Рейтинг от 0 до 5, ИНАЧЕ НЕ ДОВЕРЯЙТЕ ЭТОМУ РЕЙТИНГУ")
        self.rating = int(rating)

    def describe_restaurant(self):
        print("Название:", self.restaurantName, "Кухня:", self.cuisineType)

    def is_open_restaurant(self):
        print("Ресторан:",self.restaurantName, "- открыт")

    def rating_of_restaurant(self):
        print("Рейтинг ресторана", self.restaurantName, "-", self.rating)

    def new_rating(self, rater):
        self.rating = rater


newRestaurant = Restaurant("Michlen", "Korean", 10)
newRestaurant1 = Restaurant("Чайхона", "Среднеазиатская", 4)
newRestaurant2 = Restaurant("Макдокнакс", "***", 0)
restoList = [newRestaurant, newRestaurant1, newRestaurant2]

for restaurant in restoList:
    print("Ресторан с названием - ",restaurant.restaurantName, " и кухней - ", restaurant.cuisineType)
    restaurant.is_open_restaurant()
    print("-"*30)
    restaurant.describe_restaurant()
    print("По заданию вызывал метод выше")
    print("-"*30)
    restaurant.rating_of_restaurant()
    choiceToContinue = input("Хотите поставить новый рейтинг заведению ?\n1 - да\n2 - нет")
    if (choiceToContinue == "1"):
        rater = input("Введите новый рейтинг ресторана(от 0 до 5) : ")
        restaurant.new_rating(rater)
        restaurant.rating_of_restaurant()
    if (choiceToContinue == "2"):
        pass
