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

describe_pet('hamster', 'harry') # <--- arguments in order
describe_pet('harry', 'hamster') # <--- arguments out of order

# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')

# Default values
# def describe_pet(animal_type='dog', pet_name) <--set variable in function