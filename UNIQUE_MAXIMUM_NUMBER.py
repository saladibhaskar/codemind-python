n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
        c+=1
b.sort()
if( c==0):
    print("-1")
else:
    print(b.pop())