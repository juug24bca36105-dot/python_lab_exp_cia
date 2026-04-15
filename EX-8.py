# Aim:
# To use the re module in Python

#Code Implementation:

import re

text = "Hello, welcome to Python programming"
pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")


# Output:
#   Pattern found


# Algorithm: 
# 	Start
# 	Import the re module
# 	Define a string (text to search in)
# 	Define a pattern to search
# 	Use re.search() to check if the pattern exists
# 	If pattern is found
# 		Print “Pattern found”
# 	Else
# 		Print “Pattern not found”
# 	Stop