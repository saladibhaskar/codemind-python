n=int(input())
a=-1
b=1
c=0
mini=n
k=0
f=1
num=0
num2=0
while(k!=1):
    c=a+b
    if mini==abs(n-c) and c!=num:
        num2=c
    if abs(n-c)<mini:
        mini=abs(n-c)
        num=c
    if c>n:
        k+=1
    a=b
    b=c
if num!=0 and num2!=0:
    print(num,num2)
elif(num!=0):
    print(num)
else:
    print(num2)