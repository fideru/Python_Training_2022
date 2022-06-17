# Exceptions are type of errors that stop a program from implementing
import datetime

try:
    # The with statement will open and close external resources once the program is done
    # eliminating the need for the finally clause to close the file manually
    with open("Lists.py") as file:
        print("File opened")
    age = int(input("Age: "))
    print("You were born in the year", datetime.datetime.today().year - age)
    print("Your xfactor is", datetime.datetime.today().year / age)
except (ValueError, ZeroDivisionError) as error:
    print("You did not enter a valid age")
    print("Error type:", type(error))
else:
    print("No exceptions now")
# Always excecuted clause inside the exceptions.
finally:
    print("Closing files")
    file.close()
from timeit import timeit


code1="""def calculate_xfactor(ages):
    if ages <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / ages

# raising exceptions
# when writing your own finctions try not to insert try/except into the function
try:
    calculate_xfactor(-1)
except ValueError as error:
    pass"""

print("Code timing:", timeit(code1, number=10000))