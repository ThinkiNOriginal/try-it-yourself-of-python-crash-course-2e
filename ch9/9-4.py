class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type
        self.number_served = 0;

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def present_numbers(self):
        print(self.number_served)
    
    def set_number_served(self, val):
        self.number_served = val;
        self.present_numbers()

    def increment_number_served(self, val):
        self.number_served += val
        self.present_numbers()

    def open_restaurant(self):
        print("Open!") 
       

Arestaurant = Restaurant('A', 'B')
Arestaurant.describe_restaurant()
Arestaurant.open_restaurant()
Arestaurant.set_number_served(10)
Arestaurant.increment_number_served(5)

