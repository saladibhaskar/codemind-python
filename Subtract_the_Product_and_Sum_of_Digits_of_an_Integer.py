n=int(input())
l=list(str(n))
s=0
p=1
for i in range(len(l)):
    s+=int(l[i])
    p*=int(l[i])
print(p-s)