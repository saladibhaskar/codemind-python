n=int(input())
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
for i in range(2,n):
    if(prime(i) and prime(n//i) and i*(n//i)==n):
        print(i,n//i)
        break;
else:
    print("-1")