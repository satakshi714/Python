def recurfib(x):
    if x<=1:
        return x
    else:
        return (recurfib(x-1))+(recurfib(x-2))


x=int(input("Enter the maximum limit to generate the fibonacci series :"))
for i in range(0,x):
    print("The fibonacci series is :"(recurfib(i)))
