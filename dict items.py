a=input("data1:")
b=input("data2:")
a=a.split(",")
b=b.split(",")
d=dict(zip(a,b))
for i,j in sorted(d.items()):
    print(i,j)
