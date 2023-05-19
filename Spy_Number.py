n=int(input())
su=0
pr=1
while(n!=0):
    r=n%10
    su+=r
    pr*=r
    n=n//10
if su==pr:
    print("Spy Number")
else:
    print("Not Spy Number")