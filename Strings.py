string_variable = "Python Programming"
# len gives you the number of characters in a string
print(len(string_variable))

# [0] returns the character in the x position of a string
print(string_variable[0])
print(string_variable[-1])

# [1:5] returns the characters in the range
print(string_variable[1:5])
print(string_variable[1:])
print(string_variable[:5])
print(string_variable[:])

# Scape secuences
# \"
# \'
# \\
# \n
scape_secuence = "Python \\Programming"
print(scape_secuence)

#Formatted Strings
first = "Fidel"
last = "Baez"
print(first + " " + last)
full = f"{first} {last}"
print(full)

#string methods
print(scape_secuence.upper())
print(scape_secuence.lower())
print(scape_secuence.title())
print(scape_secuence.strip())
print(scape_secuence.index("Pro"))
print(scape_secuence.replace("P", "J"))
print("pro" in scape_secuence)
print("lol" not in scape_secuence)