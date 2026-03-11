# Aim:
#   To write a program to demonstrate control flow statements and looping statements in Python.

# Control flow statement
num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
else:
    print("Number is Negative")

# Looping statement
print("Numbers from 1 to 5:")
for i in range(1,6):
    print(i)

#output:
#   Enter a number: 5
#   Number is Positive
#   Numbers from 1 to 5:
#   1
#   2
#   3
#   4
#   5

# Algorithm:
# 	1.	Start the program.
# 	2.	Take a number as input from the user.
# 	3.	Use if–else to check whether the number is positive or negative.
# 	4.	Use a for loop to print numbers from 1 to 5.
# 	5.	Display the results.
# 	6.	Stop the program.