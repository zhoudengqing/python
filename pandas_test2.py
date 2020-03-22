'''
@Author: Dengqing zhou
@Date: 2020-03-21 23:59:49
@LastEditTime: 2020-03-22 00:10:36
@LastEditors: Dengqing zhou
@Description: pandas
@FilePath: \python\pandas_test2.py
'''
import pandas as pd

data = {'a':[1, 2, 3], 'b':[2, 3, 4], 'c':[3, 4, 5]}
frame = pd.DataFrame(data)
print(frame)