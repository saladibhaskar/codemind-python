n=int(input())
s=str(n)
for i in range(0,11):
    a=s.count(str(i))
    if(a>=2):
        print('Not Unique Number')
        break
    #print(a,end=" ")
else:
    print("Unique Number")