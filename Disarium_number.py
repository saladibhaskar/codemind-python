n=int(input())
rv=int(str(n)[::-1])
i=1
su=0
t=n
while rv!=0:
    r=rv%10
    su=su+r**i
    rv=rv//10
    i+=1
if su==t:
    print("True")
else:
    print("False")