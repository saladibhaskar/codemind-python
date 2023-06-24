t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    for i in range(0,m+1):
        if (i**2)%m==n:
            print(i,end="
")
            break
    else:
        print('-1')