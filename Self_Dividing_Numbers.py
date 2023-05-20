a=int(input())
b=int(input())
def sel(n):
    t=n
    while(n!=0):
        r=n%10
        if(r==0):
            return False
        if t%r!=0:
            return False
        n=n//10
    else:
        return True
for i in range(a,b+1):
    if(sel(i)):
        print(i,end=" ")