import numpy as np

newList1D = np.array([1, 2, 3, 4, 5 ])
newList2D = np.array([[1, 2, 3],
                        [4, 5, 6]])

# Accessing elements using indexing 
# For 1D array, use a single index
# For 2D array, use two indices: [row, column] or [row][column]
print(newList1D[0])                   # 1                  # Accessing the first element of the 1D array
print(newList2D[0, 1])                # 2                  # Accessing the element at row 0, column 1 of the 2D array
print(newList2D[1, 2])                # 6                  # Accessing the element at row 1, column 2 of the 2D array


# Slicing arrays to get subarrays
# For 1D array, use start:stop (stop is exclusive)
# For 2D array, use start:stop for rows and columns: [row_start:row_stop, col_start:col_stop]
print(newList1D[1:4])                 # [2 3 4]            # Slicing the 1D array from index 1 to 4
print(newList2D[0:2, 1:3])            # [[2, 3], [5, 6]]   # Slicing the 2D array to get a subarray
print(newList2D[:, 1])                # [2 5]              # Accessing all rows in column 1 of the 2D array


# Fancy indexing to access multiple elements
# For 1D array, use a list of indices
# For 2D array, use two lists of indices for rows and columns
print(newList1D[[0, 2, 4]])           # [1 3 5]            # Accessing multiple elements of the 1D array
print(newList2D[[0, 1], [1, 2]])      # [2 6]              # Accessing elements at (0,1) and (1,2) in the 2D array


# Boolean indexing to filter elements
# Create a boolean mask based on a condition
mask1D = newList1D > 2
mask2D = newList2D % 2 == 0
print(newList1D[mask1D])              # [3 4 5]            # Filtering elements greater than 2 in the 1D array
print(newList2D[mask2D])              # [2 4 6]            # Filtering even elements in the 2D array


# Reshaping arrays
# Use the reshape(row, column) method to change the shape of an array, Returns a new array with the specified shape
# The total number of elements must remain the same
# Reshape only works if the new shape is compatible with the original shape
reshaped2D = newList1D.reshape(5, 1)                       # Reshaping 1D array to a 2D array with 5 rows and 1 column
reshaped3D = newList2D.reshape(2, 3, 1)                    # Reshaping 2D array to a 3D array with 2 blocks, 3 rows, and 1 column
print(reshaped2D)                    # [[1], [2], [3], [4], [5]]
print(reshaped3D)                    # [[[1], [2], [3]], [[4], [5], [6]]]


# Flattening arrays
# Use the flatten() method to convert a multi-dimensional array into a 1D array, Returns a new flattened array
flattened1D_from_2D = newList2D.flatten()                 # Flattening 2D array to a 1D array
flattened1D_from_3D = reshaped3D.flatten()                # Flattening 3D array to a 1D array
print(flattened1D_from_2D)          # [1 2 3 4 5 6]
print(flattened1D_from_3D)          # [1 2 3 4 5 6]


# Raveling arrays
# Use the ravel() method to convert a multi-dimensional array into a 1D array
# Returns a flattened array, but is a view of the original array whenever possible
raveled1D_from_2D = newList2D.ravel()                     # Raveling 2D array to a 1D array
raveled1D_from_3D = reshaped3D.ravel()                    # Raveling 3D array to a 1D array
print(raveled1D_from_2D)            # [1 2 3 4 5 6]
print(raveled1D_from_3D)            # [1 2 3 4 5 6]