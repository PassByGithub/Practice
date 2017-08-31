def min(x,y):
    if x>y:
        return x
    else:return y

def distance(a,b):
    print(closet_list_x)
    print(closet_list_y)
    distance_ab=(closet_list_x[a]-closet_list_x[b])**2+(closet_list_y[a]-closet_list_y[b])**2
    print(distance_ab)
    distance_ab=distance_ab**0.5
    return distance_ab


def divide(number):
    mid_number=[]
    if len(number)==2:
        return distance(number[0],number[1])
    left_number=number[:(len(number)//2)]
    right_number=number[len(number)//2:]
    left_number_d=divide(left_number)
    right_number_d=divide(right_number)
    l=closet_list_x[len(number)//2-1]+closet_list_x[len(number)//2]
    l=l/2
    d=min(left_number_d,right_number_d)
    for i in range(len(closet_list_x)):
        if closet_list_x[i]>l-d and closet_list_x[i]<l+d:
            mid_number.append(i)
    mid_number_d=divide(mid_number)
    return min(mid_number_d,d)



def Closet_Pair():

    list1=input("Give me several points").strip(' ').split()
    closet_list=[int(x) for x in list1]
    for i in range(len(closet_list)):
        if i%2==0:
            closet_list_x.append(closet_list[i])
        else:closet_list_y.append(closet_list[i])
    number_l=[int(x) for x in range(len(closet_list_x))]
    print(number_l)
    value=divide(number_l)
    print(value)

if __name__=='__main__':
    closet_list_y=[]
    closet_list_x=[]
    Closet_Pair()