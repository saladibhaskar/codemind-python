n=int(input())
sq=n*n
ln=len(str(n))
d=sq%10**ln
if n==d:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")