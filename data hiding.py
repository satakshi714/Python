'''data hiding
fundamental concepts which provide data hiding are
1) data abstraction
It refers to the act of representing essential features without including the background
details and explainations.

2) data encapsulation
It is the way of combining both data and functions that operate on that data
under a single unit

Public and private access modifiers->
1) private
syntax:
__ (by double underscore)
A private variable can only be accessed that is of the same class and not outside of
the class
A private method can be called by the method of the same class
syntx: def__method_name()
2) Public
It can be accessed from anywhere
It can be called from anywhere
'''
class Student:
    __group="ECE"
    __report="Fail"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def setdetails(self,__group,__report):
        self.__group=__group
        self.__report=__report


    def getdetails(self):
        print(self.name,self.age,self.__group, self.__report)
        
a1=Student("abc",10)
a1.setdetails("CSE","Pass")
a1.getdetails()
print(a1.name,a1.age)
print(a1.__group,a1.__report)





'''Q5<-L7'''
