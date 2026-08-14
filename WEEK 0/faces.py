def convert(text):
    # 'text' is the receiving hand
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    # Practical 1: Passing a literal string directly
    print(convert("I am happy :)"))

    # Practical 2: Putting a string into a variable first
    mood = "I am sad :("
    result = convert(mood) # 'mood' goes into the 'text' slot
    print(result)

main()






# The Specialist (The Robot)
def convert(text):
    # It takes 'text', swaps the faces, and sends it back
    return text.replace(":)", "🙂").replace(":(", "🙁")

# The Boss (You)
def main():
    # 1. Get the input
    phrase = input()
    
    # 2. Hand the 'phrase' to 'convert' and catch the result
    result = convert(phrase)
    
    # 3. Show the result
    print(result)

# The Start Button
main()