n=int(input())
su=0
for i in range(1,n):
    if n%i==0:
        su+=i
if su==n:
    print("True")
else:
    print("False")