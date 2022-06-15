# Program to print even numbers between 1 to 10

counter = 0
for number in range (1, 18):
    if number % 2 ==0:
        counter += 1
        print(number)
print(f"We have {counter} even numbers")