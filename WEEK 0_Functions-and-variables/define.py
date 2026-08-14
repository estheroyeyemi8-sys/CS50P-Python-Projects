#Let's define a function called Hello
def hello(to = "world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)