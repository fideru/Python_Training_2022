# Program to print even numbers between 1 to 10

counter = 0
for number in range (1, 18):
    if number % 2 ==0:
        counter += 1
        print(number)
print(f"We have {counter} even numbers")


# Fizz Buzz

def fizz_buzz(digit_1):

    if (digit_1 % 5 == 0) and (digit_1 % 3 == 0):
        return "FizzBuzz"
    elif digit_1 % 5 == 0:
        return "Buzz"
    elif digit_1 % 3 == 0:
        return "Fizz"
    return "Unusable digit"


digit_1 = int(input("Enter first digit:"))
print(fizz_buzz(digit_1))