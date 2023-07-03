n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
b.sort(reverse=True)
#print(b)
if len(b)==2:
    print(b[0])
else:
    print(b[2])