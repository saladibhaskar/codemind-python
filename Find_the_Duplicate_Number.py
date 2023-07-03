n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a.count(a[i])==2:
        print(a[i])
        break