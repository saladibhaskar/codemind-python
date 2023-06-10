n=int(input())
ns=n*n
r=int(str(n)[::-1])
rs=r*r
rss=int(str(rs)[::-1])
if ns==rss:
    print("True")
else:
    print("False")