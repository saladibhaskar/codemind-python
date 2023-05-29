import math
n=int(input())
for i in range(n):
    if(i*(i+1)==n):
        print("YES")
        break
else:
    print("NO")