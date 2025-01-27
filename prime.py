a=int(input("x: "))
b=int(input("y: "))
for n in range(a,b+ 1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
        
        
'''if (n%i==0):
                continue
            print(i)'''
