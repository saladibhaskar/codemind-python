n,x=map(int,input().split())
f=int(str(n)[:x:])
b=int(str(n)[len(str(n))-x::])
print(abs(f-b))