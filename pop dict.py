a=input("data1:")
b=input("data2:")
a=a.split(",")
b=b.split(",")
d=dict(zip(a,b))
c=input("key:")
if c in d:
    e=d.pop(c)
    print(e)
    print(sorted(d.items()))
else:
    print("key does not exist")
