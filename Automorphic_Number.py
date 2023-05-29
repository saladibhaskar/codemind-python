n=int(input())
c=0
cn=0
sq=n*n
while n!=0 and sq!=0:
    r=n%10
    c+=1
    rn=sq%10
    if r!=rn :
        print("Not an Automorphic Number")
        break
    n=n//10
    sq=sq//10
else:
    print("Automorphic Number")
    
    