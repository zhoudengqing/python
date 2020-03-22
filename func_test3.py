'''
@Author: Dengqing zhou
@Date: 2020-03-21 22:10:19
@LastEditTime: 2020-03-21 22:12:19
@LastEditors: Dengqing zhou
@Description: function
@FilePath: \python\func_test3.py
'''
def a_line(a, b):
    def arg_y(x):
        return a*x+b
    return arg_y

line1 = a_line(3, 5)
line2 = a_line(5, 10)

print(line1(10))
print(line2(20))