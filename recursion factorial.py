def rec(n):
    if n==0:
        fact=1
        return fact
    else:
        fact=n*rec(n-1)
        return fact

num=int(input("num: "))
if num<0:
    print("factorial does not exist")
else:
    print("factorial: ",rec(num))
