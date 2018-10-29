class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The resturant name is " + self.restaurant_name.title() + ".")
        print("The cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is opening!")

my_restaurant = Restaurant('Lisa', 'chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant_1 = Restaurant('1', 'chinese')
restaurant_2 = Restaurant('2', 'English')
restaurant_3 = Restaurant('3', 'USA')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
