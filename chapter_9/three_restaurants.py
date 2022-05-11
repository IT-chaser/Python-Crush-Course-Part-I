class Restaurant:
    """Simple attempt to models a restaurant."""

    def __init__(res, restaurant_name, cuisine_type):
        """Initialaze name and type attributes."""
        res.name = restaurant_name
        res.type = cuisine_type

    def describe_restaurant(res):
        print(f"Restaurant name is {res.name.title()}")
        print(f"Cuisine type is {res.type}")

    def open_restaurant(res):
        print(f"{res.name} Restaurant is open")
my_res = Restaurant('Asian', 'Traditional')
next_instances = Restaurant('korean', 'modern')
next_one = Restaurant('europe', 'home cooking')
print(my_res.describe_restaurant())
print(next_instances.describe_restaurant())
print(next_one.describe_restaurant())
