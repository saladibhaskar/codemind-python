n=int(input())
su=0
while(len(str(n))!=1):
    su=0
    while(n!=0):
        r=n%10
        su=su+r*r
        n=n//10
    n=su
if su==1 or su==7:
    print(True)
else:
    print(False)