'''
@Author: Dengqing zhou
@Date: 2020-03-21 22:14:28
@LastEditTime: 2020-03-21 22:24:01
@LastEditors: Dengqing zhou
@Description: funtion
@FilePath: \python\func_test4.py
'''
def tips(func):
    def nei(a,b):
        print('start')
        func(a, b)
        print('stop')
    return nei

@tips
def add(a, b):
    print(a+b)
@tips
def sub(a, b):
    print(a-b)

print(add(4, 5))
print(sub(10, 3))