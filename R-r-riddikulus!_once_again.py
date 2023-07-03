n,r=map(int,input().split())
a=list(map(int,input().split()))
r=r%n

s=(''.join(str(i) for i in a))
if r==len(a):
    m=a
else:
    p=s[0:r:1]
    k=s[r:n:1]
    m=k+p
 
print(*list(m))