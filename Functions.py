# ############ Functions ############ #
# Parameters Inputs in functions

def greetings(first_name, last_name):
    print(f"Hello {first_name} {last_name}.")
    print("Welcome to the hood")


# 2- Types of functions
# 1- Functions that perform a task
# 2- Function that returns a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Fidel")
print(message)


# Keyword arguments (or named arguments) are values that, when passed into a function,
# are identifiable by specific parameter names

# Default arguments are arguments that have a default value unles specified
# which make the parameter in the function optional.

def value(number, by=1):
    return number + by


print(value(6,8))

# xargs add an *before the parameter in the function to give it multiple arguments
# xxargs add an *before the parameter in the function to give it multiple arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def save_user(**user):
    return user


print(save_user(id=1, name="Fidelo", age=33))

# Scope refers to the region of the code where a variable is found/used
# It applies by indentation or inside functions, classes and such
# Local and global variables: Global are variables that are usable from the whole file
# Local variables are allocated in specific functions


