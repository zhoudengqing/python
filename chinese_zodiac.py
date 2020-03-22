'''
@Author: Dengqing zhou
@Date: 2020-03-21 10:24:10
@LastEditTime: 2020-03-21 10:44:00
@LastEditors: Dengqing zhou
@Description: 记录生肖，根据年份判断生肖
@FilePath: \python\chinese_zodiac.py
'''

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

print (chinese_zodiac[0:4])

print (chinese_zodiac[-1])

year = 2018
print (year % 12)
print (chinese_zodiac[year % 12])
print ('狗' not in chinese_zodiac)
print (chinese_zodiac + 'abc')
print (chinese_zodiac * 3)
