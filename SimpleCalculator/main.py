
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

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exit...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    match choice:

        case 1:
            print(a + b)

        case 2:
            print(a - b)

        case 3:
            print(a * b)

        case 4:
            print(a / b)
            
        case 5:
            print ("Goodbye!!Exiting the programm....")
            break

        case _:
            print("Invalid option")
    
        





