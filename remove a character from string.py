a=input("string: ")
b=int(input("num: "))
c=len(a)
if b>c or b<0:
    print("num should be positive, less than the length of the string")
else:
    print((a[0:b])+(a[b+1:]))
        
