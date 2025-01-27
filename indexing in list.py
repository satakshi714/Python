1 a=input("data: ")
c=a.split(',')
print(c)
b=int(input("index: "))
if b < len(c) and b>=-len(c):
    print(c[b])
else:
    print("Invalid")
