class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"Users first name is {self.first_name} and last name is",
        self.last_name)
    def greet_user(self):
        print(f"Hello dear {self.first_name} {self.last_name}!")
#user_inst = User('John', 'Adamsons')
#print(user_inst.describe_user())
#print(user_inst.greet_user())
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
#        self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.new = Privileges()
#start = Admin('John', 'freeman')
#start.new.show_privileges()
