import numpy as np

# Creating a 1D NumPy array from a Python list
newList1D = np.array([1, 2, 3, 4, 5 ])
print(newList1D)                            # [1 2 3 4 5]


# Creating a 2D NumPy array (matrix) from a nested Python list
newList2D = np.array([[1, 2, 3], 
                      [4, 5, 6]])
print(newList2D)                        # [[1 2 3]
                                        #  [4 5 6]]


# Creating a 3D NumPy array (tensor) from a nested Python list (3D array is multiple 2D arrays)
newList3D = np.array([[[1, 2, 3],
                       [4, 5, 6]],
                      [[7, 8, 9],
                       [10, 11, 12]]])
print(newList3D)                        # [[[ 1  2  3]
                                        #   [ 4  5  6]]
                                        #  [[ 7  8  9]
                                        #   [10 11 12]]]
