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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super.__init__(restaurant_name, cuisine_type)
        self.flavor = ['sweet', 'chocolate', 'strawberry', 'milkshake']

    def describe_flavor(self):
        print("The restaurant's flavor type have " + self.flavor.title())

restaurant = IceCreamStand('only', 'chinese')
restaurant.describe_restaurant()
restaurant.describe_flavor()
