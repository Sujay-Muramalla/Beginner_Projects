""" Calculator

Set up a function that asks the User for 2 Numbers.
Create 4 different functions for + - / * 
Create another function that asks the user which mathematic operation he wants to execute
Based on that decision call the right function
BONUS: What happens if he typed in a wrong number - maybe a good thing to implement is a "cancel action"
BONUS: it'll be awesome if this program is running as long as the user does not enter the word "quit" or "exit" """



# Calculator
# User Interaction in form of: The user can choose which mathematic operation they want to perform
""" userInputNumber1 = float(input("Enter the first number: "))
userInputNumber2 = float(input("Enter the second number: ")) """

#function to get user input for numbers...
def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2


#create a function
def show_menu():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def addition():
    # put code inside
    result = number1 + number2
    return result

def complicated_algorithms():
    firstResult = addition()  # "recycle" function _> without duplicating code
    secondResult = alt_addition()
    newResult = firstResult + secondResult

def alt_addition():
    return number1 + number2

def alt_2_additon(number1: float, number2: float):
    result = number1 + number2
    return result

def subtraction(number1, number2):
    result = abs(number1-number2)
    return result

def multiply(number1, number2):
    result = number1*number2
    return result

def divide(number1, number2):
    result = number1/number2
    return result


def calculator():
    
    a, b = get_numbers()

    show_menu()
    choice = int (input("Enter choice (1/2/3/4): "))
    
    
    if choice == 1:
        result = addition(a, b)
        print("Result:", result)

    elif choice == 2:
        result = subtraction(a, b)
        print("Result:", result)

    elif choice == 3:
        result = multiply(a, b)
        print("Result:", result)

    elif choice == 4:
        result = divide(a, b)
        print("Result:", result)

    else:
        print("Invalid choice")


calculator()



""" # Global Variables
number1 = 1
number2 = 2




resultOfAddition = alt_2_additon(userInputNumber1, userInputNumber2)
print("The sum of", userInputNumber1, "and", userInputNumber2, "is:", resultOfAddition)


resultOfSubtraction = subtraction(userInputNumber1,userInputNumber2)
print("The subtraction of", userInputNumber1, "and", userInputNumber2, "is:", resultOfSubtraction)

resultOfMultiplication = multiply(userInputNumber1,userInputNumber2)
print("The Multiplication of", userInputNumber1, "and", userInputNumber2, "is:", resultOfMultiplication)

resultOfDivision = divide(userInputNumber1,userInputNumber2)
print("The division of", userInputNumber1, "and", userInputNumber2, "is:", resultOfDivision)
 """

#Michael's code
# Calculator
# User Interaction in form of: The user can choose which mathematic operation they want to perform
""" userInputNumber1 = float(input("Enter the first number: "))
userInputNumber2 = float(input("Enter the second number: "))
# Global Variables
number1 = 1
number2 = 2

def addition():
    # put code inside
    result = number1 + number2
    return result

def complicated_algorithms():
    firstResult = addition()  # "recycle" function _> without duplicating code
    secondResult = alt_addition()
    newResult = firstResult + secondResult

def alt_addition():
    return number1 + number2

def alt_2_additon(number1: float, number2: float):
    result = number1 + number2
    return result

# def subtraction():
#     # put code inside
#     result = number1 - number2
# call the function
addition()
alt_addition()
resultOfAddition = alt_2_additon(userInputNumber1, userInputNumber2)
print("The sum of", userInputNumber1, "and", userInputNumber2, "is:", resultOfAddition)
` """