from user_module import User
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
