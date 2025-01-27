def sum(a,b):
    if b==0:
        return a
    else:
        return (1+sum(a,b-1))
        
a=int(input("a: "))
b=int(input("b: "))
print("sum: ",sum(a,b))
