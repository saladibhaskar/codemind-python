n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)-1):
    if a[i]==0:
        a.remove(a[i])
        a.append(0)
for i in range(len(a)):
    print(a[i],end=" ")