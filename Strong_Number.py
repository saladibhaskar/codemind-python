n=int(input())
def fac(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
t=n
su=0
f=1
while(n!=0):
    f=1
    r=n%10
    f=fac(r)
    su+=f
    n=n//10

if su==t:
    print("The number %d is a strong number"%t)
else:
    print("The number %d is not a strong number"%t)
    