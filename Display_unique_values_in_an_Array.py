n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if(a.count(a[i])==1):
        print(a[i],end=" ")
        c+=1
if c==0:
    print("-1")