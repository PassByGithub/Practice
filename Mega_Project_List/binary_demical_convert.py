#把可能发生错误的语句放在try模块里，错误由except处理
# a=10
# b=0
# try:
#     c=a/b
#     print (c)
# except ZeroDivisionError:
#     print("done!")
# print("not done!")

#raise
# a=input("input a number")
# if not isinstance(a,int):
#     raise ValueError
# else:
#     print("no error")

#合并起来使用
def binToDec(bin_no):  #这是一个关于输入判断类型的，一般都要判断类型
    """
    @param bin_no:  an integer or str representation of a binary number
    @return:        an integer value of the binary number passed
    """
    dec = 0
    i = 0
    if not isinstance(bin_no, int): #先判断是不是
        try:
            bin_no = int(bin_no)   #不是的话判断能不能转换，不能转换的话会出现错误
        except:
            raise TypeError        #不能转换就产生一个TypeError
    while bin_no > 0:
        dec += ((bin_no % 10) * (2 ** i))
        bin_no //= 10
        i += 1
    return dec
print(binToDec(input("input a number")))
#isinstance函数
# isinstance(object, classinfo)
# 判断实例是否是这个类或者object是变量
#
# classinfo
# 是类型(tuple, dict, int, float)
# 判断变量是否是这个类型
# 其第一个参数为对象，第二个为类型名或类型名的一个列表。其返回值为布尔型。若对象的类型与参数二的类型相同则返回True。若参数二为一个元组，则若对象类型与元组中类型名之一相同即返回True。
#
# >> > isinstance(lst, list)
# True
#
# >> > isinstance(lst, (int, str, list))
# True