name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Duplex")
    case "Oluwaseyi":
        print("Mansion")
    case _: 
        print("Who?")