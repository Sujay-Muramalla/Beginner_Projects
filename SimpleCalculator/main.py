
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b




while True:

    print("\nCalculator Menu")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")

    choice = int(input("Enter choice of operation from the calculator: "))

    if choice == 5:
        print("Good bye......")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    match choice:

        case 1:
            print (add(a,b))

        case 2:
            print (subtract(a-b))

        case 3:
            print(multiply(a*b))

        case 4:
            print(divide(a/b))
            
        case _:
            print("Invalid option")
    
        





