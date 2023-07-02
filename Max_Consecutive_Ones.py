n=int(input())
a=list(map(int,input().split()))
cn=0
mx=0
for i in range(len(a)):
    if(a[i]==1):
        cn+=1
        if(cn>mx):
            mx=cn
    else:
        cn=0
print(mx)