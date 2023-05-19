n=int(input())
def add(n):
    su=0
    while(n!=0):
        r=n%10;
        su+=r
        n=n//10
    return su

while(1):
    res=add(n)
    if res<10:
        print(res)
        break
    else:
        n=res
    
    