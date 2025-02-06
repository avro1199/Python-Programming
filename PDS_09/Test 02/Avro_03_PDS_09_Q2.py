#function for calculate area

def calculate_area(radius):
    return 3.1416*(radius**2)

area = calculate_area(7)
print('Area = ', area, '\n')


#NumPy Arrays & Computations
import numpy as np

arr = np.array([5, 15, 25, 35, 45])

#add 5 by NumPy's universal function
arr = np.add(arr, 5)
print('Result => ',arr)

#Sum and mean
sum = arr.sum()
print('Sum = ', sum)

mean = arr.mean()
print('Mean = ', mean, '\n')


#Boolean Logic & Sorting

arr2 = np.array([25, 7, 18, 42, 11, 36])

idx = arr2 < 20
less_than_20 = arr2[idx]
print('Less than 20 => ',less_than_20)

arr2.sort()
print('Largest 4 numbers: ',arr2[-4:])