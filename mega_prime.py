n=int(input())
def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
if prime(n):
    while n!=0:
        r=n%10
        if not prime(r):
            print("Not Mega Prime")
            break
        n=n//10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")