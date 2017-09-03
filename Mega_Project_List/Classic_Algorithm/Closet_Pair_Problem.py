def min(x,y):
    if x>y:
        return y
    else:return x
def distance(a,b):
    distance_ab=(closet_list_x[a]-closet_list_x[b])**2+(closet_list_y[a]-closet_list_y[b])**2
    print("the distance is",distance_ab)
    distance_ab=distance_ab**0.5
    return distance_ab
def divide(number):
    if len(number)==2:
        return distance(number[0],number[1])
    if len(number)==3:
        length_number1=min(distance(number[0],number[1]),distance(number[1],number[2]))
        length_number=min(length_number1,distance(number[0],number[2]))
        return length_number
    left_number=number[:(len(number)//2)]
    right_number=number[(len(number)//2):]
    left_number_d=divide(left_number)
    right_number_d=divide(right_number)
    return min(left_number_d,right_number_d)

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
    numberx_sorted=sorted(closet_list_x)
    for i in range(len(closet_list_x)):
        location=closet_list_x.index(numberx_sorted[i])
        numbery_sorted.append(closet_list_y[location])
        number_l.append(location)
    print(number_l)
    d=divide(number_l)
    

if __name__=='__main__':
    closet_list_y=[]
    closet_list_x=[]
    numberx_sorted=[]
    numbery_sorted=[]
    Closet_Pair()
