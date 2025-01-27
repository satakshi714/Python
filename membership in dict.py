a=input("data1: ")
b=input("data2: ")
c=input("data1: ")
d=input("data2: ")

a=a.split(",")
b=b.split(",")
c=c.split(",")
d=d.split(",")

d1=dict(zip(a,b))
d2=dict(zip(c,d))
k=input("key:")
if k in d1:
    print("present in d1")
elif k in d2:
    print("present in d2")
elif k in d1 and k in d2:
    print("present in both dictionaries")
else:
    print("not present")
    
