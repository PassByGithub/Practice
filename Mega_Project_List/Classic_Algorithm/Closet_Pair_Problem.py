def min(x,y):
    if x>y:
        return y
    else:return x

def distance(x1,y1,x2,y2):
    distance_ab=(x1-x2)**2+(y1-y2)**2
    distance_ab=distance_ab**0.5
    return distance_ab

def listsort(x,y):
    list_sort=sorted(x)
    y_sorted=[]
    for i in range(len(x)):
        location=x.index(list_sort[i])
        x[location]="NONE"
        y_sorted.append(y[location])
    return list_sort,y_sorted

def divide(x_list,y_list):
    mid_xlist=[]
    mid_ylist=[]
    mid_ylist_sorted=[]
    mid_xlist_sorted=[]
    if len(x_list)==2:
        return distance(x_list[0],x_list[1])
    if len(x_list)==3:
        length_number1=min(distance(x_list[0],y_list[0],x_list[1],y_list[1]),distance(x_list[1],y_list[1],x_list[2],y_list[2]))
        length_number=min(length_number1,distance(x_list[0],y_list[0],x_list[2],y_list[2]))
        return length_number

    left_number_xlist=x_list[:(len(x_list)//2)]
    left_number_ylist=y_list[:len(x_list)//2]
    right_number_xlist=x_list[(len(x_list)//2):]
    right_number_ylist=y_list[(len(x_list)//2):]
    left_number_d=divide(left_number_xlist,left_number_ylist)
    print("left_number_d=",left_number_d)
    right_number_d=divide(right_number_xlist,right_number_ylist)
    print("right_number_d",right_number_d)

    d=min(left_number_d,right_number_d)
    l=left_number_xlist[-1]+right_number_xlist[0]
    l=l//2
    for i in range(len(x_list)):
        if x_list[i]>(l-d) and x_list[i]<(l-d):
            mid_xlist.append(x_list[i])
            mid_ylist.append(y_list[i])
    mid_ylist_sorted,mid_xlist_sorted=listsort(mid_ylist,mid_xlist)
    for i in range(len(mid_ylist_sorted)):
        for j in range(len(mid_ylist_sorted)):
            if i==j:
                pass
            if mid_ylist_sorted[j]>mid_ylist_sorted[i]-d and mid_ylist_sorted[j]<mid_ylist_sorted[i]+d:
                if ((mid_xlist_sorted[i]-l)*(mid_xlist_sorted[j]))<0:
                    d0=distance(mid_xlist_sorted[j],mid_ylist_sorted[j],mid_xlist_sorted[i],mid_ylist_sorted[i])
                    d=min(d,d0)
    return d

def Closet_Pair():
    global numberx_sorted
    global numbery_sorted
    numbery_sorted=[]
    number_l=[]
    list1=input("Give me several points").strip(' ').split()
    closet_list=[int(x) for x in list1]
    for i in range(len(closet_list)):
        if i%2==0:
            closet_list_x.append(closet_list[i])
        else:closet_list_y.append(closet_list[i])
    print(closet_list_x)
    print(closet_list_y)
    numberx_sorted,numbery_sorted=listsort(closet_list_x,closet_list_y)
    print(numberx_sorted)
    print(numbery_sorted)
    value=divide(numberx_sorted,numbery_sorted)
    print(value)

if __name__=='__main__':
    closet_list_y=[]
    closet_list_x=[]
    numberx_sorted=[]
    numbery_sorted=[]
    Closet_Pair()
