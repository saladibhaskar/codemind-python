import math
n=int(input())
a=list(map(int,input().split()))
t=1
for i in range(n):
    pro=math.prod(a)
    print(pro//a[i],end=" ")