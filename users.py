class User():
    def __init__(self, first_name, last_name, username, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address
        self.login_attempts = 0
        self.privileges = ['can add a post', 'can delete their own post', 'can modify their own post']

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

    def show_privilages(self):
        print(self.first_name.title() + " is a regular user and can only perform the following tasks:")
        for priv in self.privileges:
            print("- " + priv)