# Functions!!
def greet_user():  # <--- function
    print("Hello!")


greet_user()  # <---call to function


# Modified to specify a user
def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('jesse')


# Positional Arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')  # <--- arguments in order
describe_pet('harry', 'hamster')  # <--- arguments out of order

# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')


# Default values
# def describe_pet(pet_name, animal_type='dog') <--set variable in function

# Return Values
# def get_formatted_name(first_name, last_name, middle_name=''):
#   if middle_name:
#      full_name = first_name + ' ' + middle_name + ' ' + last_name
#    else:
#       full_name = first_name + ' ' + last_name
#    return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix') # <---last argument optional
# print(musician)


# Returning Dictionaries
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age='27')
print(musician)
