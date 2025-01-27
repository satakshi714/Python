class Employee:
    def setuid(self,id):
        self.id=id
    def getuid(self):
        return self.id

class Clerk(Employee):
    def setclerkdesignation(self,desig):
        self.desig=desig
    def getclerkdesignation(self):
        return self.desig
    
class Faculty(Employee):
    def setcourse(self,course):
        self.course=course
    def getcourse(self):
        return self.course
        

c1=Clerk()
c1.setuid(1200)
print(c1.getuid())
c1.setclerkdesignation("acc")
print(c1.getclerkdesignation())

f1=Faculty()
f1.setcourse("Python")
print(f1.getcourse())
f1.setcourse("3")
print(f1.getcourse())
