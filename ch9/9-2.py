class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, end = ' ')
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Open!") 

        

Arestaurant = Restaurant('A', 'a')
Brestaurant = Restaurant('B', 'b')
Crestaurant = Restaurant('C', 'c')
Arestaurant.describe_restaurant()
Brestaurant.describe_restaurant()
Crestaurant.describe_restaurant()
