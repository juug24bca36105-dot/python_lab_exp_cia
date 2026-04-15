# Aim:
# To calculate the average of two marks using Object-Oriented Programming.

#Code Implementation:

class Student:
    def __init__(self):
        self.marks1 = 0
        self.marks2 = 0

    def input(self):
        self.marks1 = int(input("Enter marks 1: "))
        self.marks2 = int(input("Enter marks 2: "))

    def calculate_average(self):
        avg = (self.marks1 + self.marks2) / 2
        print("Average =", avg)

s1 = Student()   

s1.input()
s1.calculate_average()

# output:
#   Enter marks 1: 75
#   Enter marks 2: 80
#   Average = 77.5


# Algorithm Steps:
# 	Start
# 		Define a class Student
# 		Declare two variables: marks1, marks2
#
# 	Create a method input()
# 		Accept values for marks1 and marks2 from the user
#
# 	Create another method calculateAverage()
# 		Compute average using formula:
#       Average = (marks1 + marks2) / 2
#
# 	Display the result
#
# 	In main() function:
# 	    Create an object of class Student
# 	    Call input() method
# 	    Call calculateAverage() method
#
# 	Stop