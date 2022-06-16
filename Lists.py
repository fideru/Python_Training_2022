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

number_list = list(range(3))
print(number_list[::2])

# ################################ #
# #######Unpacking Lists########## #
# ################################ #

first , second, third = number_list
print(first, second, third)

number_list2 = list(range(20))
one, two, *others = number_list2
print(one, two, others )

# ################################ #
# #######Looping a Lists########## #
# ################################ #
for numbers in letters:
    print(numbers)

for numbers in enumerate(letters):
    print(numbers)

# ################################ #
# ######adding to a Lists######### #
# ################################ #

list4 = ["a", "b", "c", "d", "e"]
# adding methods
list4.append("f")
print(list4)
list4.insert(3, "15")
print(list4)
# Removing items
list4.pop() # Remove last value in list
print(list4)
list4.remove("e") # Remove first one of a specific value in list
print(list4)
del list4[0:2] # Remove one or several items by position/range of values in list
list4.clear()# Remove everything from the list

# ################################ #
# ####Finding Item on a Lists##### #
# ################################ #

if "k" in list4:
    print(list4.index("k"))
else:
    print("Not available")

# ################################ #
# ####Sorting Items on a Lists#### #
# ################################ #

list5 = [1,2,3,4,5,6,7,98,234,2534,5635,25,1234,234,356,4567,657,]

list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)
print(sorted(list5))
print(list5)

items = [("Product1", 10), ("Product2", 5), ("Product3", 15)]

def sort_items(item):
    return item[1] # ! represents the second position in each tuple inside items list

items.sort(key=sort_items)
print(items)


# ################################ #
# ########Lambda Functions######## #
# ################################ #
# Lambda are simple one line functions that can be passed to another expressions
# Lambda functions are done specifying parameters:expression

items.sort(key=lambda item:item[1])
print(items)

# ################################ #
# ######## Map Functions ######### #
# ################################ #
prices = []

for i in items:
    prices.append(i[1])
print(prices)

x= map(lambda item: item[1], items)
for item in x:
    print(item)

# ################################ #
# ###### Filter Functions ######## #
# ################################ #
list6 = [("Product1", 10), ("Product2", 5), ("Product3", 15)]
evaluated = list(filter(lambda item: item[1] > 10, list6))
print(evaluated)

# ################################ #
# #### List Comprehensions ####### #
# ################################ #

# [expression for item in items]
# mapping comprehension
prices = [item[1] for item in list6]
print(prices)
# filtering comprehension
filtered = [item for item in list6 if item[1] >10]
print(filtered)

# ################################ #
# ######## Zip Function ########## #
# ################################ #

list7 = [1, 2, 3, 4, 5]
list8 = [10, 20, 30, 40, 50]

print(list(zip("abcde", list7, list8)))

# ################################ #
# ############ Stacks ############ #
# ################################ #
# LIFO last in - first out
# adding websites represented by numbers

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
last = stack.pop() # removes last value LIFO
print(last)
print(stack)
if not stack:
    print("Disable back button")

# ################################ #
# ############ Queues ############ #
# ################################ #
# FIFO behavior first in first out

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# ################################ #
# ############ Tuples ############ #
# ################################ #
# Read only lists
point = ()
print(type(point))
#Convert list to tuple
point1 = tuple([1,2,3,4,5])
print(point1)

# ################################ #
# ##### Swapping Variables ####### #
# ################################ #

a = 10
b = 12
a, b = b, a
print(a , b)

# ################################ #
# ############ Arrays ############ #
# ################################ #
# Very Large quantity list
from array import array

values = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# ################################ #
# ############# Sets ############# #
# ################################ #

