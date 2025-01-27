a=input("string: ")
b=int(input("num: "))
c=len(a)
if b>c or b<0:
    print("not valid")
else:
    print((a[0:b])*b)
