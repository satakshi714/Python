string=str(input())
if(int(string)%2!=0):
    x=string.replace(string[-1],'o')
    print(x)
else:
    print(string)
