n=int(input())
a=list(map(int,input().split()))
i=0
b=[]
while(i<len(a)):
    for j in range(a[i]):
        print(a[i+1],end=" ")
        #b.append(a[i+1])
    i+=2

