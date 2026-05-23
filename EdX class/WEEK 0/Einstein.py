def main():
    #Get mass as an integer
    m= int(input("What is the value of m? "))
    # Speed of light
    c= 300_000_000
    # Calculate E = mc^2
    # (** is the power operator in Python)
    e = m*(c**2)

    print(e)

main()