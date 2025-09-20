import numpy as np

new1DArray = np.array([1, 2, 3, np.nan])

print(np.isnan(new1DArray))                     # Output: [False False False  True]


# Replacing NaN with a specific value (e.g., 100)
arrayWithoutNaN = np.nan_to_num(new1DArray, nan=100)
print(arrayWithoutNaN)                          # Output: [  1.   2.   3. 100.]


# Check infinity values
arrayWithInf = np.array([1, 2, np.inf, -np.inf])
print(np.isinf(arrayWithInf))                   # Output: [False False  True  True]


# Replacing infinity values with a specific value (e.g., 999)
arrayWithoutInf = np.nan_to_num(arrayWithInf, posinf=999, neginf=-999)
print(arrayWithoutInf)                          # Output: [   1.    2.  999. -999.]