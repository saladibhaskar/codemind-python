import math
n=int(input())
m=int(input())
sum1=0
sum2=0
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        sum1+=i
        #print(i,end=" ")
        if(n/i!=i):
            sum1+=n/i
         #   print(n/i,end=" ")
for j in range(1,int(math.sqrt(m))+1):
    if(m%j==0):
        sum2+=j
        if(m/j!=j):
            sum2+=m/j
if(sum1-n==m and sum2-m==n):
    print("Amicable")
else:
    print("Not Amicable")