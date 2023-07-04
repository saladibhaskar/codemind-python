n=int(input())
a=-1
b=1
c=0
while(c<=n):
    c=a+b
    if c==n:
        print(True)
        break
    a=b
    b=c
else:
    print(False)
    