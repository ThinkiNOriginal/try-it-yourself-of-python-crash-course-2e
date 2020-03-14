class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, end = ' ')
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Open!") 

        
class IceCreamStand(Restaurant):

    def __init__(self, rname, rtype):
        super().__init__(rname, rtype)
        self.flavors  = ['a', 'b', 'c']

    def present_flavors(self):
        for f in self.flavors:
            print(f, end = ' ')


myice = IceCreamStand('Ice', 'en')
myice.describe_restaurant()
myice.present_flavors()
