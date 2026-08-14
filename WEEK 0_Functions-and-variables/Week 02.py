#Let's learn chaining
#chaining .strip() to remove the spaces and .upper() for the formatting
name = input("What's your name?").strip().upper()
print("Hello", name)

#splits user's name into first name and last name
user_name = input("User's name: ").capitalize()
first, last =user_name.split(" ")
print (f"Hello, {first}")
