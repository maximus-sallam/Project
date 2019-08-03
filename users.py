class User():
    def __init__(self, first_name, last_name, username, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address

    def describe_user(self):
        print("\nName: " + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("E-mail address: " + self.email_address)

    def greet_user(self):
        print("\nWelcome back, " + self.first_name.title())

max = User('maximus', 'sallam', 'maximus-sallam', 'maximus.sallam@gmail.com')
ven = User('venus', 'pondevida', 'venusseventeen', 'venuspondevida@gmail.com')
joe = User('joe', 'higgins', 'ibbit52', 'joe-thehigg-higgins52@gmail.com')
cortney = User('cortney', 'blohm', 'swedish-fish-and-meatballs', 'sweden66@swedes.com')
alex = User('alex', 'mamalakis', 'thegreekgoat', 'saganaki-mamalaki@gmail.com')
camron = User('camron', 'rawls', 'rawlsymcbawlsy','roatating-amber-warning-lights@gmail.com')

max.describe_user()
max.greet_user()
ven.describe_user()
ven.greet_user()
joe.describe_user()
joe.greet_user()
cortney.describe_user()
cortney.greet_user()
alex.describe_user()
alex.greet_user()
camron.describe_user()
camron.greet_user()