def z1():
    class Restuarant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Тип кухни ресторана {self.restaurant_name}: {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт.")

    newRestaurant = Restuarant("La Pasta", "Итальянская")
    print(f"Название ресторана: {newRestaurant.restaurant_name}.")
    print(f"Тип кухни: {newRestaurant.cuisine_type}.")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
z1()
def z2():
    class Restuarant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Тип кухни ресторана {self.restaurant_name}: {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт.")

    newRestaurant1 = Restuarant("La Pasta", "Итальянская")
    newRestaurant2 = Restuarant("ПхалиХинкали", "Грузинская")
    newRestaurant3 = Restuarant("Северянин", "Русская")

    newRestaurant1.describe_restaurant()
    newRestaurant2.describe_restaurant()
    newRestaurant3.describe_restaurant()
z2()

def z3():
    class Restuarant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Тип кухни ресторана {self.restaurant_name}: {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт.")

        def updaterating(self, new_rating):
            self.rating = new_rating
            print(f"Новый рейтинг ресторана: {self.rating}.")

    newRestaurant = Restuarant("La Pasta", "Итальянская", 4)
    print(f"Рейтинг ресторана {newRestaurant.restaurant_name}: {newRestaurant.rating}")

    newRestaurant.updaterating(5)
z3()