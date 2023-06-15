n=int(input())
def isugly(n):
    if n==1:
        return True
    elif n%2==0:
        return isugly(n//2)
    elif n%3==0:
        return isugly(n//3)
    elif n%5==0:
        return isugly(n//5)
    return False
if isugly(n):
    print('Ugly Number')
else:
    print('Not Ugly Number')