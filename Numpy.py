# Task 1 Create a 1D array numbers 1-9
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("1D Array: ")
print(array)
# Task 2 3x3 all true array
bool_array = np.ones((3, 3), dtype=bool)
print("3x3 True Matrix")
print(bool_array)
# Task 3 Extract odd numbers from array
even_array = np.arange(2, 10, 2)
print("Even Numbers Only")
print(even_array)
# Task 4. Replacing odd numbers in array
r_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in range(len(r_array)):
    if i % 2 == 0:
        r_array[i] = -1
print("Negativity over Oddness")
print(r_array)
# Task 5. Converting a 1D array into a 2D array
new_array = np.arange(0, 12).reshape(2, 6)
print("2D Array")
print(new_array)
# Task 6 Stacking two arrays and calculating totals with np.dot and np.sum
a = np.random.rand(3, 3)
b = np.random.rand(3, 3)
c = np.dot(a, b)
Sum = np.sum(c)
output = np.vstack((a, b))
print("Vertically stacked arrays A and B")
print(output)
print("Array A + B multiplied using np.dot")
print(c)
print("Adding all values together using np.sum")
print(Sum)
