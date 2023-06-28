n=int(input())
sq=n*n
s=list(str(sq))
su=0
for i in range(0,len(s)):
    su+=int(s[i])
if su==n:
    print('Neon Number')
else:
    print('Not Neon Number')