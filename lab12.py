def z1():
    class Restuarant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Тип кухни ресторана {self.restaurant_name}: {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт.")

    class IceCreamStand(Restuarant):
        def __init__(self, name, cuisine_type):
            self.flavors = []
        def display_flavors(self):
            print(" У нас есть следующие сорта мороженого:")
            for flavor in self.flavors:
                print (flavor)



    newIceCreamStand = IceCreamStand("мяу", "мяумяу")
    newIceCreamStand.flavors = ["Шоколадное", "Ванильное", "Фисташковое"]
    newIceCreamStand.display_flavors()
#z1()
def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт.")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours, rating=0):
            super(Restaurant, self).__init__()
            self.flavors = flavors
            self.location = location
            self.hours = hours
        def display_flavors(self):
            print(" У нас есть следующие сорта мороженого:")
            for flavors in self.flavors:
                print (flavors)
        def add_flavors(self, new):
            self.flavors.append(new)
            print(f"Новый сорт мороженого: '{new}'")

        def remove_flavors(self, flavors):
                self.flavors.remove(flavors)
                print(f"Cорт мороженого удалён: '{flavors}'")

        def proverka_flavors(self, flavors):
            if flavors in self.flavors:
                print(f"'{flavors} мороженое в наличии.'")
            else:
                print(f"'{flavors} мороженое не в наличии.'")
        def stick_flavors(self):
            print("Мороженое на палочке в наличии.")
        def soft_flavors(self):
            print("Мягкое мороженое в наличии.")


    newIceCreamStand = IceCreamStand("мяу", "мяумяу", ["Шоколадное", "Ванильное", "Фисташковое"], "Вознесенский проспект 44-46", "с 10:00 до 20:00", 5)
    newIceCreamStand.display_flavors()
    newIceCreamStand.add_flavors("Клубничное")
    newIceCreamStand.remove_flavors("Шоколадное")
    newIceCreamStand.stick_flavors()
    newIceCreamStand.soft_flavors()
z2()
