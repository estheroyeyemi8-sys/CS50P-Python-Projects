def main(): 
    x = input("What's the answer to the great question of Life, the Universe and Everything? ")    
    if answer(x):
        print("Yes")
    else:
        print("No")


def answer(n):
    if n == "42":
        return True
    else:
        return False


main()


answer = input("What's the answer to the great question of Life, the Universe and Everything? ")

match answer:
    case "42" | "Forty two" | "Forty-two":
        print("Yes")
    case _:
        print("No")