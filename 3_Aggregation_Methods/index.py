import numpy as np

newList1D = np.array([1, 2, 3, 4, 5 ])

print(newList1D + 2)                # [3 4 5 6 7]               # Adds 2 to each element
print(newList1D - 2)                # [-1  0  1  2  3]          # Subtracts 2 from each element
print(newList1D * 2)                # [ 2  4  6  8 10]          # Multiplies each element by 2
print(newList1D / 2)                # [0.5 1. 1.5 2.  2.5]      # Divides each element by 2
print(newList1D ** 2)               # [ 1  4  9 16 25]          # Squares each element


print(np.sum(newList1D))            # 15                        # Sum of all elements
print(np.mean(newList1D))           # 3.0                       # Mean (average)
print(np.median(newList1D))         # 3.0                       # Median (middle value)
print(np.std(newList1D))            # 1.4142135623730951        # Standard deviation
print(np.var(newList1D))            # 2.0                       # Variance
print(np.min(newList1D))            # 1                         # Minimum value
print(np.max(newList1D))            # 5                         # Maximum value
print(np.average(newList1D))        # 3.0                       # Average (mean) value