a=input("data: ")
b=int(input("element: "))
l=a.split(',')
for i in range(0,len(l)):
    l[i]=int(l[i])
count1=0
for i in range(len(l)):
    if l[i]==b:
        count1=count1+1
print(count1)
