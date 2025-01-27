#take 4 inputs from user

a=int(input())
b=int(input())
c=int(input())
d=int(input())

#print the numbers which are divisible by both 5 and 2
l=[a,b,c,d]
for i in l:
    if i%5==0 and i%2==0:
        print(i)


'''if (a%2==0 and a%5==0):
    print(a)
    continue


elif (b%2==0 and b%5==0):
    print(b)
    continue


elif (c%2==0 and c%5==0):
    print(c)
    continue


elif (d%2==0 and d%5==0):
    print(d)
    continue'''
