'''
1.several convertation between different type:

    list,tuple(不可改变的序列),diction,set{}
    int float string demical

    list2tuple:     1.list=tuple(map(lambda x:x,list))       利用迭代器原理，迭代器在range也有用到,后面的参数可以是列表和元组都可以，也可以是多个
    tuple2list:     1.li=list(map(lambda x:x,li))            map可以代替for循环吧，如果语句少
    list2set:       1.li=set(map(lambda x:x,li))
    set2list:       1.li=list(map(lambda x:x,li))
    str2list:       1.list(map(lambda x:x,a))

    list=[int (x) for x in list]#整数化
    list=[str (x) for x in list]#字符化
    数字转列表字符串
# 	while number:
# 		digits.append(number % 10)
# 		number //= 10
    a=int(a)#字符到数字
    a=str(a)#数字到字符

    ' '.join(list)  list中字符连接成新的子字符

2.Lambda:
返回的是一个函数，和def不同，def有固定的位置让写，但是lambda可以写在列表等多个地方（行为表）
应用： 1.和map()相结合：li=list(map(lambda x: x+1, li)) 对list中的元素进行转换,但是python3中map返回的是一个迭代器所以用list括起来



'''
# a=[2,1,'3']
# b=str(a[1])
# c=int(a[2])
# print(a)
# print(type(b),type(c))

# L = [lambda x: x ** 2,
#      lambda x: x ** 3,
#      lambda x: x ** 4]
#
# for f in L:
#     print(f(2))  # prints 4, 8, 16
#
# print(L[0](3))  # prints 9