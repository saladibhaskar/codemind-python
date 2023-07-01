n=int(input())
a=list(map(int,input().split()))
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
pm=1
np=1
for i in range(len(a)):
    if prime(a[i]) and a[i]!=1:
        pm*=a[i]
    else:
        np*=a[i]
print(abs(np-pm))