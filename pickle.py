'''pickling
The process to convert any kind if oython objects into byte streams(0 ans 1
)is called pickling or serialix=zation ot flattening or marshalling.
When we convert byte stream
generated through pickling) back into the python object that is known
as unpickling
Note: import pickle
for pickling use pickle.dump()
for unpickling use picle.load()
-------------------------------
import pickle
l1=[1,2,3,4,'a','b','c']
f1=open("newpickle.txt",'wb')
pickle.dump(l1,f1)
f1.close()

p1=open("newpickle.txt","rb")
o1=pickle.load(p1)
print(o1)
____________________________________________________________________________
'''

"""exception handling in python
WHile our code is being executed there might be some events that disrupt the
normal flow of your code. These events are errors.
In python an exception is a class that represents error, if these exceptions
are not handled our ptograms go into a crash state.
------------------------------
try:
    a=10
    b=0
    c=a/b
    print(c)
except:
    print("exception occured")

"""
'''
Base exception
 keyboard interrupt
  exception
    arithmetic erroe
     floating opint error
     overflow error
     zero division error
     '''
"""

-> keyboard interrupt expression is raise when you try to stop a running program
by pressing ctrl+C in a command line

try:
    inp=input()
    print("something")
except KeyboardInterrupt:
    print("Nothing")
else:
    print("lol")
    """
'''
-> zero division error
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print("exception occured")
except ValueError:
    print("idjj")
'''
"""
-> overflow error - this result is raised when the result of an arithmetic
operator is out of range
"""
'''
-> lookup error- This exception will occur if a key or inxdex in dictionary or
lisy does not exists
try a={q1
'''
"""-> name error - Is is raise when local or global name is not foumd"""

'''-> Type error- This exception is raisded when two different or unrelated
types of operands or obju=ects are combined
'''
"""-> value error- it is raised =when a built in operation or function recieves
an ag=rguments= thats has a correct type and invalid value"""

try:
    a=int(input("a: "))
    b=input("b: ")
    c=a+b
    print(c)
    d=a-b
    print(d)
    e=a/b
    print(e)
except ZeroDivisionError:
    print(" zero division typle exception occured")
except ValueError:
    print(" value error type exception occured")
except TypeError:
    print(" type error exception occured")
except Exception:
    print("Exception occued")
else:
    print("try success")
finally:
    print("Compulsory")
