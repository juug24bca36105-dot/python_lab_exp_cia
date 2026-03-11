# Aim :
#   To write a program to demonstrate list related functions in Python.

# List functions
l = [10, 20, 30]

print("Original List:", l)

l.append(40)
print("After append:", l)

l.remove(20)
print("After remove:", l)

print("Length of list:", len(l))

# output:
#   Original List: [10, 20, 30]
#   After append: [10, 20, 30, 40]
#   After remove: [10, 30, 40]
#   Length of list: 3

# Algorithm:
# 	1.	Start the program.
# 	2.	Create a list with some elements.
# 	3.	Display the original list.
# 	4.	Add an element to the list using append().
# 	5.	Remove an element using remove().
# 	6.	Display the length of the list using len().
# 	7.	Print the updated list.
# 	8.	Stop the program.