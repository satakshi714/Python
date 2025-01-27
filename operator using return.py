def solve(a,b):
    '''addition of integers'''
    c=a+b
    return c
def solve1(a,b):
    '''subtracton of integers'''
    d=a-b
    avg=(a+b)/2
    return d,avg
x=int(input("Enter first value: "))
y=int(input("Enter second value: "))

print(solve.__doc__)
print(solve(x,y))
print(solve1.__doc__)
print(solve1(x,y))
