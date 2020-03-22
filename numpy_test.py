'''
@Author: Dengqing zhou
@Date: 2020-03-21 23:47:07
@LastEditTime: 2020-03-21 23:52:44
@LastEditors: Dengqing zhou
@Description: numpy
@FilePath: \python\numpy_test.py
'''
import numpy as np

arr1 = np.array([1, 2, 3])
print (arr1)
print(arr1.dtype)

arr2 = np.array([1.2, 2.3, 3.4])
print(arr2)
print(arr2.dtype)

print(arr2 * 10)

data = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(data)
print(arr3.dtype)
print(arr3)

print(np.arange(10))
arr4 = np.arange(10)
print(arr4[5:8])