a=int(input("Enter table number: "))
b=int(input("enter the last number of table: "))
for i in range(1,b+1):
    if i<=20:
        print(a,'*',i,'=',a*i)
else:
    print("rows limited till 20")
