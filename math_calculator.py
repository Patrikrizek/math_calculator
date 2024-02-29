import os

# Clear the console
def clear_screen():
    os.system("cls||clear")

# Incorect input warning
def input_warning():
    clear_screen()
    print("Oops - incorrect input.")

# Typography - bold font
class font:
    BOLD = '\033[1m'
    END = '\033[0m'

# Math operation - addition
def addition(numbers):
    sum = 0

    for number in numbers:
        sum += number
    return sum

# Math operation - subtraction
def subtraction(numbers):
    diff = numbers[0]

    for number in range(1, len(numbers)):
        diff -= numbers[number]
    return diff

# Math operation - multiplication
def multiplication(numbers):
    product = 1

    for number in numbers:
        product *= number
    return product

# Math operation - division
def division(numbers):
    quotient = numbers[0]

    i = 0
    while i <= (len(numbers) - 2):
        quotient = quotient / numbers[(len(numbers) + (i + 1)) - len(numbers)]
        i += 1

    return round(quotient, 2)

# User values insert quest
def user_digits_request():
    user_input_numbers = str(input(f"\nPlease enter a set of " + font.BOLD + "whole" + font.END + " numbers divided by comma: "))
    numbers = user_digits_input_to_arary(user_input_numbers)

    return numbers

# User values sanitary
def user_digits_input_to_arary(user_input_numbers):
    str_numbers = user_input_numbers.split(",")
    numbers = []

    for str_number in str_numbers:
        numbers.append(int(str_number))
    return numbers

# Interface/menu
while True:
    try:
        user_choice = int(input(f"""\n{font.BOLD + "BASIC MATH CALCULATOR" + font.END}\n
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit the application
                                
Please select one of the options: """))

        if user_choice == 1:
            clear_screen()
            
            print(font.BOLD + "ADDITION" + font.END)
            numbers = user_digits_request()
            print("The sum is:", addition(numbers))

        elif user_choice == 2:
            clear_screen()
            
            print(font.BOLD + "SUBTRACTION" + font.END)
            numbers = user_digits_request()
            print("The difference is:", subtraction(numbers))
            
        elif user_choice == 3:
            clear_screen()
            
            print(font.BOLD + "MULTIPLICATION" + font.END)
            numbers = user_digits_request()
            print("The product is:", multiplication(numbers))

        elif user_choice == 4:
            clear_screen()
            
            print(font.BOLD + "DIVISIOIN" + font.END)
            numbers = user_digits_request()
            print("The quotient is:", division(numbers))

        elif user_choice == 5:
            clear_screen()
            print('Goodbye!')
            exit()

        else:
            input_warning()

    except ValueError:
        input_warning()