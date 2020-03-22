'''
@Author: Dengqing zhou
@Date: 2020-03-21 18:37:05
@LastEditTime: 2020-03-21 18:43:40
@LastEditors: Dengqing zhou
@Description: for
@FilePath: \python\test_for.py
'''
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座',
                u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
                u'处女座', u'天秤座', u'天蝎座', u'射手座')
alist = []
for i in range(1,11):
    if (i % 2) == 0:
        alist.append(i*i)
print(alist)

blist = [i*i for i in range(1,11) if(i % 2) == 0]
print(blist)

z_num = {}
z_num = {i:0 for i in zodiac_name}
print(z_num)