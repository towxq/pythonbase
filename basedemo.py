# -*- coding: UTF-8 -*-
__author__ = '01210367'
# python中的默认编码是ASCII格式 在开头加上#coding=utf-8或者# -*- coding: UTF-8 -*-即可
print '你好'
# 在 Python 里，标识符由字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
# Python 中的标识符是区分大小写的。
# python不使用{}用空格表示代码缩进  一般是4个空格 不要使用tab

# 多行是使用 \ 分为多行显示
print 'aaaaaaa'\
      'bbbbbbbb'

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

# python变量不用申明变量的类型
a = 10
b = 'asdas'
c = 10.1
# 多变量赋值
d = e = f = 3.14
g, h, i = 1, 2, 3
# python的五个标准类型
# Numbers（数字）
        #int（有符号整型）
        #long（长整型[也可以代表八进制和十六进制]）
        #float（浮点型）
        #complex（复数）
# String（字符串）
        #字符串或串(String)是由数字、字母、下划线组成的一串字符。
        #python的字串列表有2种取值顺序:
        #从左到右索引默认0开始的，最大范围是字符串长度少1
        #从右到左索引默认-1开始的，最大范围是字符串开头
        #如果你要实现从字符串中获取一段子字符串的话，可以使用变量 [头下标:尾下标]，就可以截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
# List（列表）
        # List（列表） 是 Python 中使用最频繁的数据类型。
        # 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
        # 列表用 [ ] 标识，是 python 最通用的复合数据类型。
        # 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
        # 加号 + 是列表连接运算符，星号 * 是重复操作。
# Tuple（元组）
        # 元组是另一个数据类型，类似于List（列表）。
        # 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# Dictionary（字典）
        # 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
        # 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
        # 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

str = 'Hello World!'
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

# Python逻辑运算符
    # and             x and y
    # or	          x or y
    # not             not x
# Python成员运算符
    # 除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
    # in	如果在指定的序列中找到值返回 True，否则返回 False。
    # not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
# Python身份运算符
    # 身份运算符用于比较两个对象的存储单元
    # is	is 是判断两个标识符是不是引用自一个对象
    # is not	is not 是判断两个标识符是不是引用自不同对象

# Python 条件语句
    # if 判断条件：
    #     执行语句……
    # else：
    #     执行语句……
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称

    #if 判断条件1:
    #     执行语句1……
    # elif 判断条件2:
    #     执行语句2……
    # elif 判断条件3:
    #     执行语句3……
    # else:
    #     执行语句4……
num = 5
if num == 3:            # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出


# Python 循环语句
    # while 判断条件：
    #     执行语句……
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
print "Good bye!"

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，
# 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"


# for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for letter in 'Python':     # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print '当前水果 :', fruit

print "Good bye!"

# 另外一种执行循环的遍历方式是通过索引
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]

print "Good bye!"

# for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

# break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
# break语句用在while和for循环中。
# 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句用在while和for循环中

# pass 不做任何事情，一般用做占位语句。