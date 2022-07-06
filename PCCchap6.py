# DICTIONARIES!!!
#
# Basic alien creation
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Moving alien
alien_0['speed'] = 'medium'
print(alien_0)
print("Original x-position: " + str(alien_0['x_position']))

# Move alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Looping through dictionaries
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi', }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', }

print("\n")
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title()
          + ".")

# Loop using keys() only
print("\n=====Looping with Keys=====")
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is "
              + favorite_language[name].title() + "!")

# Sorting dictionary results with the sorted() function
print("\n======Sorting dictionary results alphabetically======")
for name in sorted(favorite_language.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Loop using values() only
print("\n=====Looping with Values======")
print("The following languages have been mentioned: ")
# for language in favorite_language.values(): prints duplicates
for language in set(favorite_language.values()):  # ignores duplicates
    print(language.title())

# Nesting dictionaries
print("\n=====Nesting Dictionaries=====")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_2, alien_1, alien_0]
for alien in aliens:
    print(alien)

# Auto-generating aliens
print("\n=====Autogenerating Aliens=====")
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Upgrade first 3 aliens to level 2 then level 3
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))

# Lists in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']}  # <--toppings in a list see page 112
print("You ordered a " + pizza['crust'] + "-crust pizza" +
      " with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'], }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())

# Dictionary in a dictionary
print("\n=====Dictionary in a dictionary=====")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'enstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
