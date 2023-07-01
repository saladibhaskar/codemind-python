n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]>a[j]:
            c+=1
    print(c,end=" ")