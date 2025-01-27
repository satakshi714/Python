a=int(input("Enter a number :"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+1
if sum==a:
    print("perfect Number")
else:
    print("no one is perfect")
    
        
