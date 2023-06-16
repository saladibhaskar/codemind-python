t=int(input())
for k in range(t):
    n=int(input())
    s=int(str(n)[::-1])
    if n<0:
        print(False)
    else:
        if n==s:
            print(True)
        else:
            print(False)