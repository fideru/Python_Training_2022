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









