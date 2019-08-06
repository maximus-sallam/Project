from users import User
from admin_user import Admin, Privileges

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


max.greet_user()
max.increment_login_attempts()
print(max.login_attempts)
max.increment_login_attempts()
print(max.login_attempts)
max.increment_login_attempts()
print(max.login_attempts)
max.reset_login_attempts()
print(max.login_attempts)

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
camron.show_privilages()