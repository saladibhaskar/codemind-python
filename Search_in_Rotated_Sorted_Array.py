n=int(input())
a=list(map(int,input().split()))
t=int(input())
if a.count(t)==0:
    print('-1')
else:
    print(a.index(t))