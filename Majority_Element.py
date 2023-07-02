n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if a.count(a[i])>len(a)//2:
        print(a[i])
        break;