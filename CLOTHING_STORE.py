n=int(input())
a=list(map(int,input().split()))
t=0
k=list(set(a))
for i in range(len(k)):
    s=a.count(k[i])
    p=s//2
    t+=p
print(t)