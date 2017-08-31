
def change(A,i,j):
    b=A[i]
    A[i]=A[j]
    A[j]=b
    return A

def order(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                A=change(A,i,j)
    return A

if __name__=="__main__":
    A=input("Give me a order").strip(' ').split()
    list=[int(x) for x in A]
    print(order(list))
    print(A)