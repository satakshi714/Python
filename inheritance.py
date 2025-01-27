'''Inheritance-it is the process by which
an object of one class aquires the properties
of objects of another class
Reasons for using inhertance-
1...Reusability
2...transitive nature
If a class A inherits the property of
class B then all subclasses of A will automatically inherit
the properties of B
Syntax-
class(baseclassname:
    STATEMENT1
class derivedClassName(baseClassName):
    statement1
    statement2
    '''
class Employee:
    def setuid(self,id):
        self.id=id
    def getuid(self):
        return self
class Clerk(Employee):
    def setclerkdesignagtions(self.desig):
        self.desig=desig
    def getclerkdesignation(self):
        return self.desig
cl=Clerk()
c1.setuid(1200)
print(c2.getuid())
    
