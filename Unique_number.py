n=int(input())
s=list(set(str(n)))
sn=list(str(n))
if len(sn)==len(s):
    print('Unique Number')
else:
    print("Not Unique Number")