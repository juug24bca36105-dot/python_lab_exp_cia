# Aim:
# To visualize data using Matplotlib and Pandas.

# Code Implementation:
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Aman", "Riya", "John"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

plt.bar(df["Name"], df["Marks"])

plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()

# Output:
#   A bar graph will be displayed showing the marks of each student.
#	    Names on X-axis
#       Marks on Y-axis

# Algorithm:
# 	Start
# 	Import Pandas and Matplotlib libraries
# 	Create a dictionary with names and marks
# 	Convert the dictionary into a Pandas DataFrame
# 	Use Matplotlib to create a bar graph with names on the x-axis and marks on the y-axis
# 	Set labels and title for the graph
# 	Display the graph
# 	Stop