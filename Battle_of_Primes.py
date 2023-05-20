def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
        
a=int(input())
b=int(input())
c=a+b
i=1
while(1):
    if prime(c+i):
        print(i)
        break
    i+=1