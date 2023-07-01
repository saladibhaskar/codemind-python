n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    c.insert(b[i],a[i])
for i in range(len(c)):
    print(c[i],end=" ")