n=int(input())
m=int(input())
def fac(n):
    su=0
    for i in range(1,n):
        if n%i==0:
            su+=i
    return su    
if fac(n)==m and fac(m)==n:
    print('Amicable')
else:
    print('Not Amicable')