a=input("data1:")
b=input("data2:")
a=a.split(",")
b=b.split(",")
d=dict(zip(a,b))
l=[]
for i in d:
    l.append(d[i])
print("max:",l[-1])
print("max:",l[0])
