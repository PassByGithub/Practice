import random


def shell(a):
    circle_t=0
    single_t=0
    heads=0
    tails=0
    heads_list=[]
    tails_list=[]
    while circle_t<a[0]:
        while single_t<a[1]:
            value=random.random()
            single_t+=1
            if value>0.5:heads=heads+1
            else: tails=tails+1
        circle_t=circle_t+1
        heads_list.append(heads)
        tails_list.append(tails)
        heads=0
        tails=0
        single_t=0
    return heads_list,tails_list
if __name__=='__main__':
    a=input("Times and times").strip(' ').split()
    a=[int (x) for x in a]
    print(shell(a))