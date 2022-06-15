
temperature: int = 21
if temperature > 30:
    print("Temperature is over 30 Degrees")
    print("Drink some water boy")
elif temperature > 20:
    print("Its a noice weather")
else:
    print("Its cold bruh")
print("Done")

# ################################ #
# ########Ternary Operator######## #
# ################################ #

age = 51
#if age >= 18:
#    message = "Elegible"
#else:
#    message = "Not elegible"
#print(message)
# Better Cleaner Coding
message_better = "Elegible" if age >= 18 else "Not elegible"
print(message_better)

# ################################ #
# ########Logical Operator######## #
# ################################ #
# and (If both conditions are true then return results)
# or (If one of theb conditions is true then return results)
# not ()

high_income = True
good_credit = True
student = True

#if not high_income and good_credit:
#    print("########\nElegible")
#else:
#    print("############\nNot Elegible")

if (high_income or good_credit) and not student:
    print("########\nElegible")
else:
    print("############\nNot Elegible")

# Short Circuit Evaluation means that it will stop the evaluation
# as soon as python finds the looking value

# ################################ #
# ###Chain comparison Operators### #
# ################################ #

# if age >= 18 and age < 65: (Long redundant code)
if 18 <= age < 65:# (Cleaner code)
    print("Elegible")

# ################################ #
# ############For Loops########### #
# ################################ #

for number in range(1, 10, 2):
    print("Loop", number, (number + 1) * ".")

# for else
success = True
for number in range(3):
    print("Lulz")
    if success:
        print("Success")
        break
else:
    print("Attempted 3 times and failed")


# ############Nested Loops########### #
for x in range(1, 6, 2):
    for y in range(5):
        print(f"({x}), ({y})")

# ############ Iterables ############ #
#  means you can iterate over it for range object, strings, lists

for x in range(5):
    break

# ################################ #
# ###########While Loops########## #
# ################################ #

number = 100

while number > 0:
    print(number)
    number //=2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
else:
    print("Break Echo")

while True:
    comando = input(">")
    if comando.lower() == "quit":
        break

