# While loops!!!
# Parrot keeps talking until quit is entered
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Adding flag to signal if program should run or not
active = True  # <----flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
       print(message)
print("\n")

# While loop with dictionaries and lists
# Start with users that need to be verified
# and an empty list to hold confirmed users
uncofirnmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
# Move each verified user to the list of confirmed users
while uncofirnmed_users:
    current_user = uncofirnmed_users.pop()
    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users
print("\nThe following users have been verified: ")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())

# Removing multiple values within a list
print("\n")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
for pet in pets:
    print(pet)

# Filling dictionary with user input
print("\n")
responses = {}

# Set flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb today? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")