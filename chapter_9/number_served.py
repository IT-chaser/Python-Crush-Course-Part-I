class Restaurant:
    """Simple attempt to models a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialaze name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}")
        print(f"Cuisine type is {self.type}")

    def number_of_costmers(self):
        print(f"Number of costmers are {self.number_served}")

    def open_restaurant(self):
        print(f"{self.name} Restaurant is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, new_served_costmers):
        self.number_served += new_served_costmers
restaurant = Restaurant('Asian', 'Traditional')
restaurant.set_number_served(34)
restaurant.increment_number_served(3)

print(restaurant.number_of_costmers())
#print(my_res.open_restaurant())
