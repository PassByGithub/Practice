def factorial(x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        return x*factorial(x-1)

if __name__=='__main__':
    x=int(input("Tell me the number"))
    print(factorial(x))