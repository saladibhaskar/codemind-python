n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
t=int(input())
c=0
for i in range(len(a)):
    if t>=a[i] and t<=b[i]:
        c+=1
print(c)