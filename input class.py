class Salary:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getname(self):
        return(self.name)
    def getsalary(self):
        return(self.salary)
    
p1=input("name:")
p2=input("salary:")
A1=Salary(p1,p2)
#A2=Salary(p2)
print("name:",A1.getname(),"salary:",A1.getsalary())
