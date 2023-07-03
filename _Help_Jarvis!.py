t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in str(n)]
    c=0
    a.sort()
    for i in range(len(a)-1):
        if a[i+1]-a[i]==1:
            c+=1
        else:
            print("NO")
            break;
    else:
        print("YES")