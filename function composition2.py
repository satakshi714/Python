def square(x):
    x=x**2
    return x
def double(x):
    x=x*2
    return x
def add(x):
    x=x+1
    return x
x=int(input("num: "))
print(add(double(square(x))))


