#Ask the user for a text review of their rider
def convert(text):
    return text.replace(":)","🙂").replace(":(", "🙁")


def fee_to_int(f):
    clean_f = f.replace("N", "")  # Strips the 'N'
    return int(clean_f)           # Converts to an integer number


def main():
    #Ask the user for a text review of their rider
    review = input("Give a review of your rider ")
    #convert to an emoji 
    result = convert(review)
    print(result)

# Handle the fee
    user_fee = input("What is the delivery fee amount? ")
    clean_fee = fee_to_int(user_fee)  # Calls the function we added above
    
    # Calculate the 10% bonus using the CORRECT variable name
    tip = clean_fee * 0.10
    
    # Added the missing 'f' here so the math actually displays
    print(f"Rider Bonus: N{tip:.0f}")


# Run the program
main()