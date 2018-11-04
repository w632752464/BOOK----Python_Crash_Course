class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The resturant name is " + self.restaurant_name.title() + ".")
        print("The cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is opening!")

    def served_number(self):
        print("The restaurant have served " + str(self.number_served) + " people.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        self.number_served += num

restaurant = Restaurant('Lisa', 'chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.served_number()

restaurant.number_served = 35
restaurant.served_number()

restaurant.set_number_served(55)
restaurant.served_number()

restaurant.increment_number_served(100)
restaurant.served_number()

# restaurant_1 = Restaurant('1', 'chinese')
# restaurant_2 = Restaurant('2', 'English')
# restaurant_3 = Restaurant('3', 'USA')
#
# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()
