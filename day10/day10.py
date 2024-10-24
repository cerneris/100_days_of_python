# Calculator

# Sum, multiply, divide, subtract
def sum(a, b):
    if type(a) != float:
        a = float(a)
    if type(b) != float:
        b = float(b)
    return a + b

def multiply(a, b):
    if type(a) != float:
        a = float(a)
    if type(b) != float:
        b = float(b)
    return a * b

def divide(a, b):
    if type(a) != float:
        a = float(a)
    if type(b) != float:
        b = float(b)
    return a / b

def subtract(a, b):
    if type(a) != float:
        a = float(a)
    if type(b) != float:
        b = float(b)
    return a - b

def menu():
    print("Let's calculate! Choose your option: ")
    print("1 : SUM")
    print("2 : MULTIPLY")
    print("3 : DIVIDE")
    print("4 : SUBTRACT")
    print("5 : EXIT")
    return input("Choice: ")

while True:
    choice = menu()
    match choice:
        case "1":
            print("You choosed SUM")
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The result of your calculation {a} + {b} = {sum(a, b)}")
        case "2":
            print("You choosed MULTIPLY")
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The result of your calculation {a} * {b} = {multiply(a, b)}")
        case "3":
            print("You choosed DIVIDE")
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The result of your calculation {a} / {b} = {divide(a, b)}")
        case "4":
            print("You choosed SUBTRACT")
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The result of your calculation {a} - {b} = {subtract(a, b)}")
        case "5":
            print("Exiting..")
            break
        case _:
            print("Incorrect choice! Try again.")