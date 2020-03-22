'''
@Author: Dengqing zhou
@Date: 2020-03-21 21:10:50
@LastEditTime: 2020-03-21 21:24:16
@LastEditors: Dengqing zhou
@Description: except
@FilePath: \python\exception_handling.py
'''
try:
    year = int(input('input year:'))
except (ValueError, AttributeError, KeyError):
    print('年份要输入数字')
    
try:
    print (1/0)
except ZeroDivisionError:
    print ('0 不能作为除数！')