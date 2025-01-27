a=input()
b=a[0]
c=a[1]
d=a[-1]
e=a[-2]
if b==d and c==e:
    print(b+c+e+d)
elif(b==e and c==d):
    print(b+c+e+d)
else:
    print(a[2:4])
