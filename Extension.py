# Task 1 Creating pattern 111222333123123123
import numpy as np
a = np.arange(1, 4)
rep1 = 3
b = np.repeat(a, rep1)
d = np.arange(1, 4)
rep2 = 3
e = np.tile(d, rep2)
f = np.concatenate((b, e))
print("Numpy Patterns: ", f)

# Task 2 Removing repeat values in Array B
array_a = np.arange(1, 6)
array_b = np.arange(4, 10)
ab_array = np.concatenate((array_a, array_b))
print("Arrays A and B: ", ab_array)
final_array = np.unique(ab_array).tolist()
print("Removing Duplicates: ", final_array)

# Task 3 Sum of all values between 5 and 10
filter_array = ab_array >= 5
new_array = ab_array[filter_array]
print("Arrays A and B: ", ab_array)
print("Array Values 5 and above: ", new_array)
Sum = np.sum(new_array)
print("Sum of Array: ", Sum)
