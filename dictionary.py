a=input("data1:")
b=input("data2:")
c=a.split(",")
d=b.split(",")
print(c)
print(d)
dict=dict(zip(c,d))

print("Dictionary:",sorted(dict.items()))
