n=int(input())
a=list(map(int,input().split()))
s=int(input())
c=0
b=[]
for i in range(s):
    b.append(a[i])
    b.append(a[i+s])
print(*b)