#Merge_sort
import os


a=input("Enter the sequence you want to sort").strip(' ').split()
#这边是一个测试输入是否正确的模块
try:
    list_test=[int(x) for x in a]
except:
    print("game is over")
    os._exit(0)

list1=[int(x) for x in a]
if len(list1)%2:
    list1.append(0)

list3=[]

for i in range(0,len(list1)//2):
    if list1[i*2]>list1[i*2+1]:
        a=list1[i*2]
        list1[i*2]=list1[i*2+1]
        list1[i*2+1]=a
print(list1)
def min(x,y):
    if x>y:
        return y
    elif x<=y:
        return x

# def compare(list_1,list_2):
#     global x
#     for i in list_2:
#         for j in list_1:
#             list3.append(min(i,j))
#     if x-1==len(list1):
#         return list_1
#     x=x+2
#     next_list=list1[x:x+2]
#     return compare(list3,next_list)

def compare(list_1,list_2):
    list4=[]
    while list_1 and list_2:
        #改进
        # if list_1[0]>list_2[0]:list4.append(list_1.pop(0))
        # else:list4.append(list_2.pop(0))
        a=list_1[0]
        b=list_2[0]
        c=min(a,b)
        if c in list_1:
            list_1.remove(c)#如果已经知道位置的话可以直接用pop，pop还能对返回值进行操作
        else:list_2.remove(c)
        list4.append(c)
    #可以尽量不用if 语句：
    #list4=list4.extend(list_1)
    #list4=list4.extend(list_2)
    if list_1:
        list4=list4+list_1
    if list_2:
        list4=list_2+list4
    return list4


for i in range(0,(len(list1)//2)):
    compare_list=list1[i*2:i*2+2]
    list3=compare(list3,compare_list)
list3.remove(0)
print(list3)

#去重且保留原序操作
# l1 = ['a',1,'c','b',2,'b','c','d','a']
# 2 l2= sorted(set(l1),key=l1.index)
# 3 print('l2:',l2)
# 4 print('l1:',l1)