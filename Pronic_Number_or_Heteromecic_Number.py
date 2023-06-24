import math
n=int(input())
r=int(math.sqrt(n))
for i in range(1,r+2):
    #print(r)
    if i*(i+1)==n:
        print("YES")
        break
else:
    print("NO")