#simple class
# class person:
#     pass
# p=person()
# print(p)#在person类的__main__模块中有了一个obejcet

#method in class
# class person:   #类
#     def say_hi(self):   #类的method ，方法
#         print('hello world')
# p=person()
# p.say_hi()#p是对象，但是也可以有方法

#__init__method in class
# class person:
#     def __init__(self,name):#__init__method是类的对象被实例化后立即执行，name是字段，对象和类都可以拥有，是变量；字段在类中就是类变量，在对象里就是实例变量
#         self.name=name#self的用处是区别类方法和函数，所以在类的参数列表开头一定要写上self；self就成了一个对象，self.name中的name是self中的一个字段，和右边的局部变量name不一样
#     def say_hi(self):
#         print('hello world',self.name)
# p=person('myluck')
# p.say_hi()#对象可以用属于类中的method
# print(p.name)#name是这个

#类变量和对象变量的局别
# class Robot:
#     population=0  #population属于类变量
#     def __init__(self,name):
#         self.name=name#name变量属于self对象，__init__方法会初始化一个名字给每个对象
#         print("Initializing()".format(self.name))
#         Robot.population+=1
#     def die(self):
#         print('{} is died'.format(self.name))
#         Robot.population-=1
#     @classmethod#调用装饰器，即将后面的这个方法标记为类方法
#     #how_many=classmethod(how_many),这个意思同上，标记成类方法
#     def how_many(cls):#属于类而不属于对象，是一个静态方法
#         print('{} is still alive'.format(Robot.population))
#         print('{} is still alive'.format(self.__class__.population))#self.__class__是引用self对象所在的类

#inherit
class schoolmember:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        print('Initialized members:{}'.format(self.name))
    def tell(self):
        print('name:{},age:{}'.format(self.name,self.age),end=' ')
class teacher(schoolmember):#表明teacher是一个子类，基类是schoolmember
    def __init__(self,age,name,salary):
        #调用基类的方法
        schoolmember.__init__(self,age,name)#显性调用了schoolmember里的init,但是如果你不写的话，python会直接调用schoolmember里的init
        self.salary=salary
        print('Initialized teachers:{}'.format(self.name))
    def tell(self):
        print('name:{},age:{},salary:{}'.format(self.name,self.age,self.salary),end=' ')
class students(schoolmember):
    def __init__(self,age,name,mark):
        schoolmember.__init__(self,age,name)
        self.mark=mark
        print('Initialized students:{}'.format(self.name))
    def tell(self):
        print('name:{},age:{},mark:{}'.format(self.name,self.age,self.mark),end=' ')

# t=teacher('Henrry',25,10000)
# s=students('Emma',12,98)
# schoolmember.tell()
t = teacher('Mrs. Shrividya', 40, 30000)#定义类的时候，后面要带上一个包含类的名称的一个元组
s = students('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()#子类和基类中有同名的方法时，先从当前类中找，没找到回基类中找
