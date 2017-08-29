'''
Project 1:Find PI to the Nth Digit
Time:2017.8.28
Algorithm:Chudnovsky Algorithm  https://en.wikipedia.org/wiki/Chudnovsky_algorithm

Module Dependencies:

Math provides with square rooting
Decimal give the Decimal data type which is better than Float

'''

import math
import sys
from decimal import *
from functools import reduce
getcontext().rounding=ROUND_HALF_DOWN#ROUND_CEILING是天花板，进一位，ROUND_DOWN或者FLOOR是舍去，half down就是四舍五入
sys.setrecursionlimit(10000)#本身python迭代次数是几百的样子，可以人工社会成10000

def factorial(x):

    '''
    Return the Factorial of a number using recursion

    parament x:the number to get factorial of
    '''
    # value=1
    # for i in range(1,x+1):
    #     value=value*i
    # #print(value)
    # return value

    # if not x:
    #     return 1
    # return x*factorial(x-1)
    return reduce(lambda x,y:x*y,[1]+list(range(1,x+1)))#在python2.X中range返回的是一个列表，但在3中返回的是一个列表，所以要用list(range(1,3))表示成一个列表
                            #[1]也不能去掉，因为list这边是一个方法
def calcu(k):

    '''
    Calculation of pi based on Chudnovsky Algorithm
    :param k:number of decimal digits to get
    :return:modified pi
    '''

    k=k+1
    getcontext().prec = k
    sumup=1
    #sumup=0
    for i in range(1,k):#range4 =[0,1,2,3]
        # Mk = factorial(6 * i) / (factorial(3 * i) * (factorial(i)) ** 3)
        # Lk = 545140134 * i + 13591409
        # Xk = (640320) ** (3 * i)

        D=(factorial(i))
        sumup=sumup+(Decimal.from_float(1)/Decimal.from_float(D))
    print(type(sumup))#加完之后这个数据类型也变成了decimal
    return sumup

def show(k):

    '''
    print the result
    '''

    D=calcu(k)
    # print(D)
    # C=426880*math.sqrt(10005)
    # print(Decimal.from_float(C))
    # result=(Decimal.from_float(C))/D    #只有demical/demical才会体现出来？
    # print(result)
    print(D)

if __name__=='__main__':
    number=int(input("Enter the number of digits upto which the value of Pi should be calculated"))
    show(number)