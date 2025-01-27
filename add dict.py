a=input("data1: ")
b=input("data2: ")
e=input("data1: ")
f=input("data2: ")


a=a.split(",")
b=b.split(",")
e=e.split(",")
f=f.split(",")


for i in range(len(a)):
    a[i]=int(a[i])
    
for i in range(len(b)):
    b[i]=int(b[i])

for i in range(len(e)):
    e[i]=int(e[i])
    
for i in range(len(f)):
    f[i]=int(f[i])
    
d1=dict(zip(a,b))
d2=dict(zip(e,f))

dict3={}
for key in sorted(d1)+sorted(d2):
    dict3[key]=d1.get(key,0)+d2.get(key,0)
print(sorted(dict3.items()))
