# lists are put inside brackets[]

letters = ["a", "b", "c", "d", "e","f"]
matrix = [[2, 11], [13, 2]]
zeros = [0] * 10
combined = zeros + matrix
print(combined)
numbers = list(range(150))
chars = list("Hello World")
print(chars)
print(len(chars))
print(letters[0:3])
# list comprehension
# [expression for item in items]
letters = {x * 2 for x in range(5)}
print(letters)

# Sets
# Sets are collection of values with no duplicates
# Sets are unordered collections, meaning that cannot be accessed by index(specific positioning)

nnumbers = [1,2,3,4,4]
first = set(nnumbers)
second = {1, 5}
print(nnumbers)
second.add(6)
second.remove(1)
len(second)
print(second)
#print(nnumbers | second) # returns new set including both sets
#print(nnumbers & second) # returns set with values that exist in both sets
#print(nnumbers - second) # returns set with values not repeated in first set
#print(nnumbers ^ second) # retunrs set with values not repeated in both sets


# Dictionaries
# A dictionary is a collection of key value pairs (Matching key info with values)

#point_dictionary = {"Name": "John", "Phone": "859-589-8547"}
point_dictionary = dict(name="John", phone="859-589-8547")
point_dictionary["gender"] = "Male" # add one more key value to dictionary
point_dictionary["name"] = "Juan" # change value of key in dictionary
# Search for a specific key in a dictionary
if "a" in point_dictionary:
    print("a")
#print(point_dictionary.get("a", 0)) # returns 0 as a result in case of not found
#del point_dictionary["a"] # deletes a key in the dictionary
# looping dictionaries
for key in point_dictionary:
    print(key, point_dictionary[key])
for x in point_dictionary.items():
    print(x)
# Dictionary comprehensions
values1 = {x: x * 2 for x in range(5)}
print(values1)
# Generator Expressions
# are iterable object generators

# Unpacking Operator
numbers = [1, 2, 3]
print(*numbers) # the * works as an unpacking of the list.
print([*range(5), *"Hello"])
# can unpack lists, strings, dictionaries, tuples



