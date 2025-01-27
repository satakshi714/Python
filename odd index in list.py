a=input("data: ")
l=a.split(',')
for i in range(0,len(l)):
    l[i]=int(l[i])
list=[]
for i in range(len(l)):
    if i%2!=0:
        list.append(l[i])
print(l[i])
