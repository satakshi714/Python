'''take an integer n from the user find out whether the given integer
is odd or even using recursion'''
def check(n):
    if (n < 1):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print("Number is even!")
else:
      print("Number is odd!"
