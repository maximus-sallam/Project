def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

my_name = get_formatted_name(input("What's your first name? "),
                             input("What's your last name? "),
                             input("What's your middle name? "))
print(my_name)

# def do_math(a, b):
#     total = a + b
#     return total
#
# math = do_math(3,3)
# print(math)



