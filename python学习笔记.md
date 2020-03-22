<!--
 * @Author: Dengqing zhou
 * @Date: 2020-03-21 10:01:41
 * @LastEditTime: 2020-03-22 00:45:43
 * @LastEditors: Dengqing zhou
 * @Description: 
 * @FilePath: \python\python学习笔记.md
 -->

# python 学习

## 基本数据类型

- 整数(int)
- 浮点数(float)
- 字符串(string)
- 布尔值(bool)

## 变量

- var=123 用=号赋值

## 序列

### 字符串 

- 用''或""括起来
- "abcd"

### 列表

- 用[]括起来
- [0, "abcd"]

### 元组

- 用()括起来，存储的内容一般不可变更
- ("abcd", "xyz")

### 序列的基本操作

- in，not in成员关系操作符
- 连接操作符 +
- 重复操作符 *
- 切片操作 [:]

## 条件判断

### if

1. if 表达式 :
        代码块
2. if 表达式 :
        代码块
    else :
        代码块
3. if 表达式 :
        代码块
    elif 表达式 :
      代码块
    else :
        代码块

### for

for 迭代变量 in 迭代对象 :
    代码块

### while

while 表达式 :
    代码块

## 映射的类型

### 字典

- 定义

{"哈希值":"对象"}
{'length':180, 'width':80}

## 文件操作

- 打开 open
- 读 read
- 写 write
- 读取一行 readlines
- 读取文件指针当前位置 tell
- 修改文件指针位置 seek 0-文件开头 1-当前位置 2-文件结尾

## 异常处理

try:
    <监控异常>
except Exception[,reason]:
    <异常处理代码>
finally:
    <无论异常是否发生都执行>

## 函数

- 定义

def 函数名称():
    代码
    return 函数返回的内容

- 可变长参数 def func(first, *other)
- filter 过滤器
- iter 迭代器
- yield 生成器
- lamda lamda表达式
- zip 
- 闭包
- 装饰器

## 类class

- 定义

class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def print(self):
        print ('%s: %s' %(self.name, self.hp))

## 多线程

- import threading 
- t1 = threading.Thread()
- t1.start()

## 正则表达式

- re模块

## 日期相关的模块

- time
- datetime

## 数学库

- math模块
- random模块 产生随机数

## 文件夹操作库

- os

## numpy

## pandas

## matplotlib

## tensorflow

## 网络库

### urllib

- from urllib import request  
- url = 'http://www.baidu.com'
- response = request.urlopen(url, timeout=1)
- print (response.read().decode('utf-8'))

### requests

### BeautifulSoup

### 网页的两种请求方式

- get
- post