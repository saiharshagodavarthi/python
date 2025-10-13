program-1
---------

Syntax: 
# import numpy as np 
# np.array([elements]) 
# np.add(array1, array2) 
# np.greater(array1, array2) 
# np.zeros(shape) 
# np.ones(shape) 
# np.linspace(start, stop, num) 
# array.tolist() 
 
Program: 
import numpy as np 
arr = np.array([1, 2, 2, 3, 4, 4, 4, 5]) 
print("Original array:", arr) 
print("\nUsing repr():") 
print(repr(arr)) 
print("\nUsing count():") 
arr_list = arr.tolist() 
print("Count of 4 in array:", arr_list.count(4)) 
print("\nUsing np.bincount():") 
print("Element counts (by index):", np.bincount(arr)) 
print("\nUsing np.unique():") 
unique_elements, counts = np.unique(arr, return_counts=True) 
print("Unique elements:", unique_elements) 
print("Counts:", counts) 
----------------------------------------------------------------------------------------------------------------------

program-2
--------

Program: 
import numpy as np 
arr = np.array([4, 7, 2, 9, 2, 7, 5, 9, 2]) 
print("Array:", arr) 
value = 5 
greater_than_value = arr[arr > value] 
less_than_value = arr[arr < value] 
print("\nNumbers greater than", value, ":", greater_than_value) 
print("Numbers less than", value, ":", less_than_value) 
max_value = np.max(arr) 
min_value = np.min(arr) 
max_index = np.argmax(arr) 
min_index = np.argmin(arr) 
print("\nMaximum Value:", max_value) 
print("Minimum Value:", min_value) 
print("Index of Maximum Value:", max_index)
print("Index of Minimum Value:", min_index) 
count_values = np.bincount(arr) 
unique_values, counts = np.unique(arr, return_counts=True) 
print("\nFrequency count using bincount:", count_values) 
print("Unique values:", unique_values) 
print("Counts of unique values:", counts) 

----------------------------------------------------------------------------------------------------------




