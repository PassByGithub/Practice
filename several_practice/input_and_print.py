#simple input
# def reverse(text):
#     return text[::-1]#文本倒过来
# def is_palindrome(text):
#     return text==reverse(text)
# while True:
#     text = input('Enter someting')
#     if is_palindrome(text):
#         print('it is a palindrome')
#         exit()
#     else:
#         print('it is not a plaindrome')

# def reverse(text):
#     return text[::-1]#文本倒过来
# def is_palindrome(texts):
#     return texts==reverse(texts)
# while True:
#     text = input('Enter someting')
#     text=set(text)
#     if ',' in text:
#       text.remove(',')
#     elif ' ' in text:
#       text.remove(' ')
#     else:
#         pass
#     text=[text]
#     if is_palindrome(text):
#         print('it is a palindrome')
#         exit()
#     else:
#         print('it is not a plaindrome')


poems = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开文件以编辑（'w'riting）
f = open('poem.txt', 'w')# 创建一个poem.txt文件并且往里面写东西
# 向文件中编写文本
f.write(poems)
# 关闭文件
f.close()
#
# # 如果没有特别指定，
# # 将假定启用默认的阅读（'r'ead）模式，默认的而且默认文件一般是txt
# f = open('poem.txt')
# while True:
#     line = f.readline()，读一串完整的行
#     # 零长度指示 EOF
#     if len(line) == 0:
#         break
#     # 每行（`line`）的末尾
#     # 都已经有了换行符，自动换行
#     #因为它是从一个文件中进行读取的
#     print(line, end='')
# # 关闭文件
# f.close()
#
# import pickle
# shoplistfile='shoplistname'
# shoplist=['mango','apple','grape']
# f=open(shoplistfile,'wb')
# pickle.dump(shoplist,f)  #写入过程叫封装
# f.close()
# del shoplist
# f=open(shoplistfile,'rb')
# shoplist=pickle.load(f)  #读出过程叫拆封
# print(shoplist)

#当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们的 Unicode 字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”。
#这时候用encoding="utf-8"作为关键词参数加入我们的open函数中
#encoding=utf-8
# import io
# f=io.open('abc.txt',"wt",encoding="utf-8")
# f.write(u"hello world")
# f.close()
#
# text=io.open("abc.txt",encoding="utf-8").read()
# print(text)

#try……except 处理异常
# a=10
# b=0
# try:
#     c=a/b
#     print (c)
# except ZeroDivisionError:
#     print('wrong')
# print('done!')

# encoding=UTF-8

#raise引发一个异常
# class ShortInputException(Exception):#这个异常类必须是Exception的子类
#     '''一个由用户定义的异常类'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# try:
#     text = input('Enter something --> ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)#引发一个较做shortinputexception的异常类
#     # 其他工作能在此处继续正常运行
# except EOFError:
#     print('Why did you do an EOF on me?')
# except ShortInputException as ex:#引发了一个异常后，将这个异常定义为ex，即名字
#     print(('ShortInputException: The input was ' +
#            '{0} long, expected at least {1}')
#           .format(ex.length, ex.atleast))
# else:
#     print('No exception was raised.')

#try……final
# import sys
# import time
#
# f=None
# try:
#     f = open("poem.txt")
#     # 我们常用的文件阅读风格
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         sys.stdout.flush()#输出打印
#         print("Press ctrl+c now")
#         # 为了确保它能运行一段时间
#         time.sleep(2)#进入两秒休眠
# except IOError:
#     print("Could not find file poem.txt")
# except KeyboardInterrupt:
#     print("!! You cancelled the reading from the file.")
# finally:  #这是程序结束前最后的指令
#     if f:
#         f.close()
#     print("(Cleaning up: Closed the file)")

#with
#在try中获取资源，然后在finally快中释放资源是一种常见的模式
with open("poem.txt") as f: #with获取open返回的对象即thefile，当代码块执行开始时调用thefile.__enter__函数，结束用thefile.__exit__函数
    for line in f:
        print(line, end='')
#避免了try finally的重复使用