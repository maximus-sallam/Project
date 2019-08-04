class User():
    def __init__(self, first_name, last_name, username, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address
        self.login_attempts = 0
        # self.privileges = ['can add a post', 'can delete their own post', 'can modify their own post']

    def describe_user(self):
        print("\nName: " + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("E-mail address: " + self.email_address)

    def greet_user(self):
        print("\nWelcome back, " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    # def show_privilages(self):
    #     print(self.first_name.title() + " is a regular user and can only perform the following tasks:")
    #     for priv in self.privileges:
    #         print("- " + priv)

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

max = Admin('maximus', 'sallam', 'maximus-sallam', 'maximus.sallam@gmail.com')

max.describe_user()
max.privileges.show_privileges()

print("\nAdding privileges...")
admin_privileges = [
    'can add a post',
    'can delete any post',
    'can modify any post',
    'can ban any user',
    'can have sex with any user'
    ]

max.privileges.privileges = admin_privileges
max.privileges.show_privileges()


ven = User('venus', 'pondevida', 'venusseventeen', 'venuspondevida@gmail.com')
joe = User('joe', 'higgins', 'ibbit52', 'joe-thehigg-higgins52@gmail.com')
cortney = User('cortney', 'blohm', 'swedish-fish-and-meatballs', 'sweden66@swedes.com')
alex = User('alex', 'mamalakis', 'thegreekgoat', 'saganaki-mamalaki@gmail.com')
camron = User('camron', 'rawls', 'rawlsymcbawlsy','roatating-amber-warning-lights@gmail.com')


# max.greet_user()
# max.increment_login_attempts()
# print(max.login_attempts)
# max.increment_login_attempts()
# print(max.login_attempts)
# max.increment_login_attempts()
# print(max.login_attempts)
# max.reset_login_attempts()
# print(max.login_attempts)
# max.show_privilages()

# ven.describe_user()
# ven.greet_user()

# joe.describe_user()
# joe.greet_user()

# cortney.describe_user()
# cortney.greet_user()

# alex.describe_user()
# alex.greet_user()

# camron.describe_user()
# camron.greet_user()