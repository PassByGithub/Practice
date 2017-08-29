#derive two values from function
# def get_two_values():
#     return (2,'two')# 返回一个元组
# a,b=get_two_values()
# print(a)
# print(b)
# a,b=b,a #b,a是另一个元组
# print(a,b)

#不想缩进就把语句写到一行去
# flag=True
# if flag:print("yes"）
#一般是块里面的语句只有一句

#List Comprehension 列表推导
# listone=[2,3,4]
# listtwo=[i*2 for i in listone if i>2]
# print(listtwo)
# 上下两种对比，用简洁点好
# listone=[2,3,4]
# listtwo=[]
# for i in listone:
#     if i>2:
#         listtwo.append(i*2)
# print(listtwo)
# def powersum(power, *args):
#     total=0
#     for i in args:
#         total+=pow(i,power)
#     return total
# power=int(input("Enter a tower"))
# a,b=map(int,input("Enter two numbers").strip().split())#map引用一个函数和可迭代对象，比如列表，然后对该对象进行操作，split是input的分割的方法，strip的话也是去掉某一个东西比如空格啥的
#int是一个函数, 这是元组从str到int的过程，str也是一个函数
# power_args=(a,b)
# value=powersum(power,power_args)
# print(value)
#这段程序是错的！pow这个函数有待考究

#assert语句
# mylist=['items']
# assert len(mylist)>=1#但是没有办法断定这个assert是否为真
# mylist.pop()
# assert len(mylist)>=1

