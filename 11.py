def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт")
    newRestaurant=Restaurant("Фиро","итальянская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт")
    a=input("Название ресторана ")
    b=input("Тип кухни ")
    rest1=Restaurant(a, b)
    a = input("Название ресторана ")
    b = input("Тип кухни ")
    rest2 = Restaurant(a, b)
    a = input("Название ресторана ")
    b = input("Тип кухни ")
    rest3 = Restaurant(a, b)
    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest3.describe_restaurant()
def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_reyt):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_reyt = restaurant_reyt
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт")
        def chang_reyt(self, newreyt):
            print(f"Изначальный рейтинг ресторана {self.restaurant_name} {self.restaurant_reyt}")
            self.restaurant_reyt = newreyt
            print(f"Рейтинг ресторана обновлён {self.restaurant_reyt}")
            print(f"Новый рейтинг ресторана {self.restaurant_name} {self.restaurant_reyt}")
    rest1 = Restaurant("tpo", "italic", "5")
    a = input("Новый рейтинг ")
    rest1.chang_reyt(a)
z1()
z2()
z3()