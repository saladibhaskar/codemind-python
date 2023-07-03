n=int(input())
m=int(input())
s=0
s1=0
for i in range(n):
    s=sum(list(map(int,input().split())))
    s1=s1+s
print(s1)