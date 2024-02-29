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