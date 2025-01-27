a=int(input())
b=int(input())
c=int(input())

#print the 2nd smallest number

list=[a,b,c]
list.sort()
length=len(list)
print(list[length-2])
