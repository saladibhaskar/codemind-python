n,m=map(int,input().split())
i=n
while(1):
    if i%n==0 and i%m==0:
        print(i)
        break
    i+=1