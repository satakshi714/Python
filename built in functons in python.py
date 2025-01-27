a=input("data1: ")
b=input("data2: ")
a=a.split(",")
b=b.split(",")
d=dict(sorted(zip(a,b)))
print("all(dict):",all(d))
print("any(dict):",any(d))
print("len(dict):",len(d))
print("sorted(dict):",sorted(d))
print("sorted dictionary:")
for i,j in sorted(d.items()):
    print(i,j,sep=":")
    
