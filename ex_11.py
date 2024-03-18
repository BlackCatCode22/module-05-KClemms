# findall() retains a list of all matches

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# returns an empty list if no matches
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# finds the first white space in the line
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# Example of when request doesn't have a match
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


# Example of a split at each white space character
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# Splits only at the first occurrence 
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


# Replaces white space with the requested character
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# Replaces the first 2 occurrences
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


# Returns a matched object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


# Returns any words with an uppercase S
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


# Passes a string into a function
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# Prints the part of the string where there was a match
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 