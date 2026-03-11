# Aim:
#   To write a program to demonstrate dictionary related functions in Python.

d = {"name": "Susmita", "age": 20}    
print("Original Dictionary:", d)
d["city"] = "Kolkata"
print("After adding city:", d)
del d["age"]
print("After deleting age:", d)
print("Keys:", d.keys())
print("Values:", d.values())

#output:
#   Original Dictionary: {'name': 'Susmita', 'age': 20}
#   After adding city: {'name': 'Susmita', 'age': 20, 'city': 'Kolkata'}
#   After deleting age: {'name': 'Susmita', 'city': 'Kolkata'}
#   Keys: dict_keys(['name', 'city'])
#   Values: dict_values(['Susmita', 'Kolkata']) 
 
# Algorithm:
# 	1.	Start the program.
# 	2.	Create a dictionary with some key-value pairs.
# 	3.	Display the original dictionary.
# 	4.	Add a new key-value pair to the dictionary.
# 	5.	Delete a key-value pair from the dictionary.
# 	6.	Display the keys and values of the dictionary.
# 	7.	Print the updated dictionary.
# 	8.	Stop the program.
