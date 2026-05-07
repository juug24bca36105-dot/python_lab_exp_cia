 Q. Write a Program to Implement Various Types of Visualization in Python
Aim:
To implement different types of visualization using Python.
code
import matplotlib.pyplot as plt

# Sample Data
students = ["A", "B", "C", "D"]
marks = [80, 90, 70, 85]

# Line Chart
plt.plot(students, marks)
plt.title("Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Scatter Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

Output
Displays:
1. Line Chart
2. Bar Chart
3. Pie Chart
4. Scatter Plot
