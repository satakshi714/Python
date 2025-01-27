'''comment'''
def solve(a,b):
    '''addition of integers'''
    c=a+b
    print(a,'+',b,'=',c)
def solve1(a,b):
    '''subtracton of integers'''
    d=a-b
    print(a,'-',b,'=',d)
def solve2(a,b):
    '''multiplication of integers'''
    e=a*b
    print(a,'*',b,'=',e)
def solve3(a,b):
    '''division of integers'''
    f=a/b
    print(a,'/',b,'=',f)
def solve4(a,b):
    '''floor division of integers'''
    g=a//b
    print(a,'//',b,'=',g)
def solve5(a,b):
    '''modulus of integers'''
    h=a%b
    print(a,'%',b,'=',h)
def solve6(a,b):
    '''exponent of integers'''
    i=a**b
    print(a,'**',b,'=',i)

x=int(input("Enter first value: "))
y=int(input("Enter second value: "))

print(solve.__doc__)
solve(x,y)
print(solve1.__doc__)
solve1(x,y)
print(solve2.__doc__)
solve2(x,y)
print(solve3.__doc__)
solve3(x,y)
print(solve4.__doc__)
solve4(x,y)
print(solve5.__doc__)
solve5(x,y)
print(solve6.__doc__)
solve6(x,y)


