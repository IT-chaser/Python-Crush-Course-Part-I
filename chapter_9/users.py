class User:
    def __init__(user, first_name, last_name):
        user.first_name = first_name
        user.last_name = last_name
    def describe_user(user):
        print(f"Users first name is {user.first_name} and last name is",
        user.last_name)
    def greet_user(user):
        print(f"Hello dear {user.first_name} {user.last_name}!")
user_inst = User('John', 'Adamsons')
print(user_inst.describe_user())
print(user_inst.greet_user())
