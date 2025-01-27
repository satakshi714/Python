''' Raising an exception- In pytho na programmer can actually raise a builtin exception
or user defined exception in a try block

def checkage(age):
    if age<0:
        raise ValueError("age should be greater than or equal to zero")
    else:
        print("age is valid")

try:
    age=int(input("enter ager: "))
    checkage(age)
except ValueError as e:
    print(e.args)
finally:
    print("Final Block")

'''

''' User defind exception- exceptions can have custom messages based on
what has to be displayed, such exceptions are calles user defined
exceptions All user defined exceptions have to be derrivies derived from
exception or base exception class

class OurException(Exception):
    def __init__(self,message):
        self.message=message
class UsingUserException:
    try:
        a=int(input("enter a: "))
        b=int(input("enter b: "))
        if b==0:
            raise OurException("b should b greater than 0")
        c=a//b
        print("answer is ",c)
        
    except OurException as e:
        print(e.message)
        
'''

'''Regular Expression- A regular expression is a sequence of
characters that defines a search pattern
import re
pattern='^j...k$'
test_string="jfbdk
result=re.mathc(patter,test_string)
'''

'''Meta characters = these are the characters that are inperpreted in a special way
by regular expression engine
1) []- This specifies a set of characters you wish to match'''
