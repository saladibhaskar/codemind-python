n=int(input())
a=list(map(int,input().split()))
su=0
for i in range(n):
    su+=a[i]
for i in range(n,0,-1):
    if su%i==0:
        print(i)
        break

    