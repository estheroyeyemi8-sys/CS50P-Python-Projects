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