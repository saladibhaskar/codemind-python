n=int(input())
a=list(map(int,input().split()))
b=list(map(lambda x:x**2,a))
b.sort()
for i in range(len(b)):
    print(b[i],end=" ")