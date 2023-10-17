a = input()
v = 0
c = 0

for i in range(len(a)):
    if a[i] in ['a', 'e', 'i', 'o', 'u']:
        v += 1
        if v == 1:
            c = 0
            print("V", end="")
    elif 'a' <= a[i] <= 'z':
        c += 1
        if c == 1:
            v = 0
            print("C", end="")
