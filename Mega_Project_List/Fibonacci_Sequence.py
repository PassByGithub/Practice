'''
Project 3:Fibonacci_Sequence
Time:2017.8.28
Algorithm:No

Module:
Fibonacci(k) provide the Fibonacci Sequence
Show(k)      print the result
'''
#own program
# def Fibonacci(k):
#     Fibonaccilist=[1,1]
#     k=k+1
#     for i in range(3,k):
#         sum=Fibonaccilist[i-2]+Fibonaccilist[i-3]
#         Fibonaccilist.append(sum)
#     return Fibonaccilist
#
# def show(k):
#     showlist=[]
#     showlist=Fibonacci(k)
#     print(showlist)
#
# n=int(input('up to which do you want the Fibonacci Sequence to?'))
# print(type(n))
# show(n)
#Q：
#刚开始input前面没有加int，导致输入的n即k，为str类型，和int型的1无法相加出现错误

def fibSequence(n):
    """
    Generates a fibonacci sequence
    with the size of n
    """
    assert n > 0 #确保n>0

    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    series=map(str,series)#将列表里的类型进行转换 int 转为str

    return(', '.join(series))  # Return the sequence seperated by commas
    #返回的是字符串,输出一个列表join

def main():  # Wrapper function

    print(fibSequence(int(input('How many numbers do you need? '))))
    #打印一个
if __name__ == '__main__':
    main()