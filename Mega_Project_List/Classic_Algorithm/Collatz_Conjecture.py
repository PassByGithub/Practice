import os
import sys

def reach(number):
    counter=0
    if number<=1:
        try:sys.exit(0)
        except:
            print("the number is not true")
    while number!=1:
        if number%2==0:number//=2
        else:number=number*3+1
        counter=counter+1
    return counter

if __name__=='__main__':
    number=input("Enter a number which is bigger than 1")
    try:int(number)
    except:
        print("The number is not a integer")
        os._exit(0)
    number=int(number)
    print(reach(number))
    print(number)