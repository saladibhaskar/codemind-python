k=int(input())
def pal(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
for s in range(k):
    n=int(input())
    i=n
    while(1):
        #print(i)
        if(pal(i)):
            n1=i
            s1=abs(n-i)
            break
        else:
            i+=1
    i=n
    while(1):
        if(pal(i)):
            n2=i
            s2=abs(n-i)
            break
        else:
            i-=1 
    if(s1==s2):
        print(min(n1,n2))
    elif(s1>s2):
        print(n2)
    else:
        print(n1)