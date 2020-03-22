'''
@Author: Dengqing zhou
@Date: 2020-03-21 21:40:10
@LastEditTime: 2020-03-21 21:44:40
@LastEditors: Dengqing zhou
@Description: function
@FilePath: \python\func_test.py
'''
def func (a, b, c):
    print ('a= %s' %a)
    print('b= %s' %b)
    print('c= %s' %c)
func(1, 2, 3)

def howlong(first, *other):
    print (1 + len(other))
howlong(1, 2, 3, 4, 5)