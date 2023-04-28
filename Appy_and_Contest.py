t=int(input())
for y in range(t):
    n,a,b,k=map(int,input().split())
    c=a*b
    d=n/c
    e=n/a
    f=n/b
    if e+f-d>=k:
        print("Win")
    else:
        print("Lose")
        
