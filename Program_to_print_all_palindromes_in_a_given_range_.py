a=int(input())
b=int(input())
def pal(n):
    s=str(n)[::-1]
   # print(n,s)
    if str(s)==str(n):
        return True
    else:
        return False

for i in range(a,b+1):
    if(pal(i)):
        print(i,end=" ")
