n=int(input("n: "))
import math
pi=math.pi
for i in range (1,n+1):
    print("{:.{}f}".format(pi,i))
