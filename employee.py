class Employee():

    def __init__(self, first_name, last_name, annual_salary):
        self.annual_salary = annual_salary
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.happy = self.full_name + ' earns enough money and is very happy.'
        self.unhappy = self.full_name + ' is not happy with his ' + \
                       str(self.annual_salary) + ' salary.'

    def give_raise(self, amount=5000):
        self.annual_salary += amount

    def show_salary(self):
        return str(self.annual_salary)

    def show_happiness(self):
        if self.annual_salary < 75000:
            return self.unhappy
        else:
            return self.happy