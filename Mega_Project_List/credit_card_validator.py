# def tell(changelist):
#     changelist=[2*int(x) for x in changelist]
#     print(changelist)
#     sum=-1
#     for i in changelist:
#         sum+=1
#         if i>=10:
#             changelist[sum]=i%10+i//10
#     return changelist

#我一直想的都是很复杂的操作，其实可以直接在一个数组里完成
def shell():
    initlist=list(input("tell me the number").strip(' ').split())
    # changedlist=[initlist[-i] for i in range(1,len(initlist)+1)]#把整个数字倒过来
    if len(initlist)%2==0:
        oddoreven=1 #偶数
    else:oddoreven=0
    initlist=[int(x) for x in initlist]#把列表整数处理

    for i in range(len(initlist)):
        if oddoreven:#偶数
            if i%2:
                initlist[i]=initlist[i]*2
        else:
            if i % 2:
                initlist[i]=initlist[i]*2
        if initlist[i]>=10:
            initlist[i]=initlist[i]%10+initlist[i]//10
    print(sum(initlist))#sum可以直接求列表数的总和

if __name__=='__main__':
    shell()