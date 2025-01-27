#take 2 float inputs from user

p=float(input("P: "))
q=float(input("q: "))

#product of input

product=(p*q)
a=format(p,'.6f')
b=format(product,'.6f')

#print outputs upto 6 decimal places

print("p={},q={},product={}".format(a,q,b))
