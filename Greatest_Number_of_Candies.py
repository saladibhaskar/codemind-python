n=int(input())
a=list(map(int,input().split()))
k=int(input())
mx=max(a)
b=[]
for i in range(len(a)):
    if a[i]+k>=mx:
        print(True,end=" ")
    else:
        print(False,end=" ")