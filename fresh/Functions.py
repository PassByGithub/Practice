# #function1
# def say_hello():
#     print('hello world')
# say_hello()
# say_hello()

#function2
# def sq(a):
#     a=a*a
#     return a
# number=5
# number=sq(number)
# print(number)

#function 3
# def print_max(a,b):         #parameters是形参的意思，定义函数时给定的名称叫做parameters
#     if a>b:
#         print(a,'is maximum')
#     else:
#         print(b,'is maximum')
# print_max(3,4)
# x=5
# y=7
# print_max(x,y)              #arguments是实参的意思，调用的时候所提供给函数的值
#

#local variables
# x=50
# def func(x):
#     x=2
#     print('x is',x)
# func(x)
# print('x actually is',x)

#global variables
# x=50
# def func():
#     global x
#     x=2
#     print('x is',x)
# func()
# print('x actually is',x)

#function_default
# def say(message,times=1):#times就是一个parameter
#     print(message*times)#字符串乘以数字等于复制
#     print(message)
# say('hello')
# say('bye',5)

#keyword arguments
# def func(a,b=10,c=10):
#     print('a is',a,'and b is',b,'c is',c)
# func(4,6)
# func(2,c=5)

#function_varargs

# def total(a,*number,**diction):   #**指的是字典的意思,*则是元组
#     print('a', a)
#     for i in number:
#         print(i)
#     for first_part,second_part in diction.items():
#         print(first_part,second_part)
# total(10,1,2,3,Jack=1123,John=2231,Henry=1560)

#function_docstrings
# def total(a,*number,**diction):   #**指的是字典的意思,*则是元组
#     '''wendang zifuchuan hahahahahahahaha kandonglema'''
#     print('a', a)
#     for i in number:
#         print(i)
#     for first_part,second_part in diction.items():
#         print(first_part,second_part)
# total(10,1,2,3,Jack=1123,John=2231,Henry=1560)
# print(total.__doc__)#help()函数也就是打印出了文档字符串

