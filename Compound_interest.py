import math
p,r,t=map(float,input().split())
c=p*(pow((1+r/100),t))
print("%.2f"%c)