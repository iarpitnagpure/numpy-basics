import numpy as np

new1d_array = np.array([1, 2, 3, 4, 5])
new2d_array = np.array([[1, 2, 3], 
                        [4, 5, 6]])


# insert(array, index, value, axis=None)
# insert allows you to insert a value at a specified index in the array.
# axis None means the array is flattened before insertion, 1 means insertion along rows, and 0 means insertion along columns.
print(np.insert(new1d_array, 2, 10))                # [ 1  2 10  3  4  5]                   # Insert 10 at index 2
print(np.insert(new2d_array, 1, 10, axis=0))        # [[ 1  2  3] [10 10 10] [ 4  5  6]]    # Insert 10 at index 1 along the first axis
print(np.insert(new2d_array, 1, 10, axis=1))        # [[ 1 10  2  3] [ 4 10  5  6]]         # Insert 10 at index 1 along the second axis

# append(array, value, axis=None)
# append is similar to insert but always adds to the end of the array.
# axis None means the array is flattened before appending, 1 means appending along rows, and 0 means appending along columns.
print(np.append(new1d_array, 10))                          # [ 1  2  3  4  5 10]                    # Append 10 to the end
print(np.append(new2d_array, [[10, 11, 12]], axis=0))      # [[ 1  2  3] [ 4  5  6] [10 11 12]]     # Append a new row
print(np.append(new2d_array, [[10], [11]], axis=1))        # [[ 1  2  3 10] [ 4  5  6 11]]          # Append a new column


# concatenate((array1, array2), axis=0)
# concatenate joins two arrays along a specified axis.
# axis 0 means joining along rows, and 1 means joining along columns.
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((array1, array2), axis=0))   # [[1 2] [3 4] [5 6] [7 8]]    # Concatenate along rows
print(np.concatenate((array1, array2), axis=1))   # [[1 2 5 6] [3 4 7 8]]        # Concatenate along columns


# delete(array, index, axis=None)
# delete removes an element at a specified index from the array.
# axis None means the array is flattened before deletion, 1 means deletion along rows, and 0 means deletion along columns.
print(np.delete(new1d_array, 2))                # [1 2 4 5]                      # Delete element at index 2
print(np.delete(new2d_array, 1, axis=0))        # [[1 2 3]]                      # Delete row at index 1
print(np.delete(new2d_array, 1, axis=1))        # [[1 3] [4 6]]                  # Delete column at index 1


# stacking arrays
# vstack((array1, array2)) stacks arrays vertically (row-wise).
# hstack((array1, array2)) stacks arrays horizontally (column-wise).
array3 = np.array([9, 10, 11])
array4 = np.array([11, 12, 13])
print(np.vstack((array3, array4)))     # [[ 9 10 11] [11 12 13]]                # Vertical stack
print(np.hstack((array3, array4)))     # [ 9 10 11 11 12 13]                    # Horizontal stack


# splitting arrays
# split(array, indices_or_sections, axis=0) splits an array into multiple sub-arrays.
# axis 0 means splitting along rows, and 1 means splitting along columns.
array5 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8]])
print(np.split(array5, 2, axis=1))     # [array([[1, 2], [5, 6]]), array([[3, 4], [7, 8]])]   # Split into 2 sub-arrays along columns
print(np.split(array5, 2, axis=0))     # [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]       # Split into 2 sub-arrays along rows