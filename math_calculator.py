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
def division(dividend, divisor):
    quotient = round(dividend / divisor, 2)

    return quotient