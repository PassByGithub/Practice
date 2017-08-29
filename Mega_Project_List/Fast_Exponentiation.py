def sq(a,b):
    i=2
    if b==1:
        return a
    if not b%2==0:
        return ((sq(a,(b-1)//2))**2)*a
    return (sq(a,b//2)**2)

def shell():
    l=input("Tell me the number").strip(' ').split()
    a=int(l[0])
    b=int(l[1])
    print(sq(a,b))

if __name__=='__main__':
    shell()