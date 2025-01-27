a=int(input())
i=a
while i>9:
    print(i%10,end=" ")
    i=i//10
print(i%10)
print(a%10)
