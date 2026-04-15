# Aim: 
# To use NumPy and Pandas packages in Python.

# Code Implementation:

import numpy as np
import pandas as pd

# NumPy part
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)
print("Sum of array:", np.sum(arr))

# Pandas part
data = {
    "Name": ["Aman", "Riya", "John"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# Output:
#   NumPy Array: [1 2 3 4 5]
#   Sum of array: 15
#   Pandas DataFrame:
#      Name  Marks
#   0  Aman     85
#   1  Riya     90
#   2  John     78

# Algorithm:
# 	Start
# 	Import NumPy and Pandas libraries
# 	For NumPy:
# 		Create a NumPy array with some integers
# 		Print the array
# 		Calculate and print the sum of the array elements
# 	For Pandas:
# 		Create a dictionary with names and marks
# 		Convert the dictionary into a Pandas DataFrame
# 		Print the DataFrame
# 	Stop