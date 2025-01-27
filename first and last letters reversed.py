a=input("string: ")
b=(a[0])
c=(a[1:-1])
d=(a[-1])

if len(a)==0:
    print("null")
elif len(a)==1:
    print(a)
else:
    print(d+c+b)
