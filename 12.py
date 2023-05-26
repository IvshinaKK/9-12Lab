def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors=flavors
        def flavors_chek(self):
            print(f"Сорта мороженого {self.flavors}")
    newRestaurant = IceCreamStand("Кафе-мороженое", "итальянская", "ванильное, пломбир, фисташковое")
    print(newRestaurant.flavors_chek())
def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт")
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors=flavors
            self.location=location
            self.time=time
        def flavors_chek(self):
            print(f"Виды в наличии {self.flavors}")
        def del_flavors(self):
            a=self.flavors.split(",")
            for i in range(len(a)):
                a[i]=a[i].strip()
            b=input("Какой вкус мороженого закончился? ")
            if b in a:
                a.remove(b)
                self.flavors=a
                print("Вкус ", b, "удалён.\n В наличии вскусы:", self.flavors)
            else:
                self.flavors = a
                print("Такого вкуса не было в наличии изначально")
            return ""
        def add_flavors(self):
            a=self.flavors
            '''
            a = self.flavors.split(",")
            for i in range(len(a)):
                a[i] = a[i].strip()
            '''
            b=input("Введите новый вкус мороженого: ")
            a.append(b)
            self.flavors=a
            print("Вкус ", b, "добавлен.\n В наличии вскусы:", self.flavors)
            return ""
        def test_flavors(self):
            a = self.flavors
            b = input("Какой вкус проверить на наличие? ")
            if b in a:
                print("Вкус ", b, "в наличии")
            else:
                print("Вкус ", b, "в не наличии")
            return ""
    newRestaurant = IceCreamStand("Кафе-мороженое", "итальянская", "ванильное, пломбир, фисташковое", "г. Спб, ул. Невского, д.56", "11:00-23:00")
    print(newRestaurant.del_flavors())
    print(newRestaurant.add_flavors())
    print(newRestaurant.test_flavors())
    class soft_IceCream(IceCreamStand):
        def __init__(self, flavors):
            self.flavors=flavors
            self.type="Мягкое мороженое"
        def soft(self):
            print(f"Вкус мороженого {self.flavors} \nТип мороженого {self.type}")
            return ""
    class ise_IceCream(IceCreamStand):
        def __init__(self, flavors):
            self.flavors = flavors
            self.type="Лёд"
        def ise(self):
            print(f"Вкус мороженого {self.flavors} \nТип мороженого {self.type}")
            return ""
    mor=soft_IceCream("клубничное")
    print(mor.soft())
    mor=ise_IceCream("Клубничный")
    print(mor.ise())



from tkinter import *
def z3():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors=flavors
        def flavors_chek(self):
            print(f"Виды в наличии {self.flavors}")
            a = self.flavors.split(",")
            for i in range(len(a)):
                a[i] = a[i].strip()
            w=Tk()
            w['bg']='#ffffff'
            w.geometry('320x100')
            #can=Canvas(w,height=320, width=100, background='#ffffff', borderwidth=0)
            #can.pack()
            w.title('Вкусы мороженого')
            for i in range (len(a)):
                vk=Label(w,text=a[i],background='#ffffff', justify="left")
                vk.pack()
            w.mainloop()
            return ""
    newRestaurant = IceCreamStand("Кафе-мороженое", "итальянская", "ванильное, пломбир, фисташковое")
    print(newRestaurant.flavors_chek())

z1()
z2()
z3()