n=int(input())
a=list(map(int,input().split()))
s=list(set(a))
mx=0
num=0
num2=0
for i in range(len(s)):
    c=0
    c=a.count(s[i])
    if c>mx:
        mx=c
        num=s[i]
    if c==mx and s[i]!=num and s[i]<num:
        num2=s[i]
if num2==0:
    print(num)
else:
    print(num2)
    