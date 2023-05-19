n=int(input())
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
cn=0
for i in range(1,n+1):
    if(n%i==0 and  not prime(i)):
        cn+=1
print(cn+1)