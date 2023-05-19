n=int(input())
pro=1
su=0
while(n!=0):
    r=n%10
    su+=r
    pro*=r
    #print(r)
    n=n//10

if su==pro:
    print("Spy Number")
else:
    print("Not Spy Number")