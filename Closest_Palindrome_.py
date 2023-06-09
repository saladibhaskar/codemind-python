n=int(input())
i=n+1
def pal(n):
    rev=int(str(n)[::-1])
    if rev==n:
        return True
    else:
        return False
while(1):
    #print(i)
    if(pal(i)):
        n1=i
        s1=abs(n-i)
        break
    else:
        i+=1
i=n-1
while(1):
    if(pal(i)):
        n2=i
        s2=abs(n-i)
        break
    else:
        i-=1 
if(s1==s2):
    print(n2,n1)
elif(s1>s2):
    print(n2)
else:
    print(n1)