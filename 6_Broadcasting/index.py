import numpy as np

new1DArray = np.array([1, 2, 3])
new2DArray = np.array([[1, 2, 3], 
                       [4, 5, 6]])


# Broadcasting (Only possible when dimensions are compatible)
# Adding 1D array to 2D array
# The 1D array is "stretched"/"expanded" to match the shape of the 2D array
# Resulting array will have the shape of the 2D array
array3 = new1DArray + new2DArray
print(array3)               # Output: [[2 4 6] [5 7 9]]

array4 = new2DArray - new1DArray
print(array4)               # Output: [[0 0 0] [3 3 3]]

# Multiplying 1D array with 2D array
array5 = new1DArray * new2DArray
print(array5)               # Output: [[ 1  4  9] [ 4 10 18]]


# Adding a scalar to a 1D array
# The scalar is added to each element of the array
array6 = new1DArray + 1
print(array6)               # Output: [2 3 4]

# Multiplying a scalar with a 2D array
# Each element of the array is multiplied by the scalar
array7 = new2DArray * 2
print(array7)               # Output: [[ 2  4  6] [ 8 10 12]]


# Vector and Matrix Operations
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Adding a vector to each row of the matrix
result1 = matrix + vector
print(result1)              # Output: [[ 2  4  6] [ 5  7  9] [ 8 10 12]]


# Subtracting a vector from each row of the matrix
result2 = matrix - vector
print(result2)              # Output: [[ 0  0  0] [ 3  3  3] [ 6  6  6]]


arrayA = np.array([1, 2, 3])
arrayB = np.array([1, 2, 3, 4])
# The following operation will raise an error due to incompatible shapes
# arrayC = arrayA + arrayB
# print(arrayC)              # This will raise a ValueError