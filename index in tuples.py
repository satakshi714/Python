a=input("data:")
b=a.split(',')
'''for i in range(0,len(b)):
    b[i]=int(b[i])'''
i=int(input("index:"))
v=input("value:")
if i not in b:
    print("enter valid index")
else:
    b[i]=v
    c=tuple(b)
    print("tuple:",c)
