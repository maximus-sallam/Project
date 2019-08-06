from users import User

class Admin(User):
    def __init__(self, first_name, last_name, username, email_address):
        super().__init__(first_name, last_name, username, email_address)
        # self.privileges = ['can add a post', 'can delete any post', 'can modify any post', 'can ban any user', 'can have sex with any user']
        self.privileges = Privileges()

    # def show_privilages(self):
    #     print(self.first_name.title() + " is an Admin user and can perform the following tasks:")
    #     for priv in self.privileges:
    #         print("- " + priv)

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for priv in self.privileges:
                print("- " + priv)
        else:
            print("- This user has no privileges.")