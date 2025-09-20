import numpy as np

newList1D = np.array([1, 2.3, 3, 4, 5 ])
newList2D = np.array([[1, 2, 3], 
                      [4, 5, 6]])
newList3D = np.array([[[1, 2, 3],
                       [4, 5, 6]],
                      [[7, 8, 9],
                       [10, 11, 12]]])

# Using the shape attribute to get the dimensions of the arrays
print(newList1D.shape)                   # (5,)             # 5 is the number of elements in the 1D array
print(newList2D.shape)                   # (2, 3)           # 2 is the number of rows, and 3 is the number of columns
print(newList3D.shape)                   # (2, 2, 3)        # 2 is the number of 2D arrays, 2 is the number of rows, and 3 is the number of columns

# Using the dtype attribute to get the data type of the array elements
print(newList1D.dtype)                   # float64
print(newList2D.dtype)                   # int64 (or int32 depending on the system)
print(newList3D.dtype)                   # int64 (or int32 depending on the system)

# Using the ndim attribute to get the number of dimensions of the arrays
print(newList1D.ndim)                    # 1
print(newList2D.ndim)                    # 2
print(newList3D.ndim)                    # 3

# Using the size attribute to get the total number of elements in the arrays
print(newList1D.size)                    # 5
print(newList2D.size)                    # 6
print(newList3D.size)                    # 12

# Using the astype() method to convert the data type of the array elements
newList1D_int = newList1D.astype(int)
print(newList1D_int)                     # [1 2 3 4 5]
print(newList1D_int.dtype)               # int64 (or int32 depending on the system)
 