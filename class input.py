class Student:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def getname(self):
        return(self.name)
    def getaddress(self):
        return (self.address)
    
Student1=Student("Izzy","NYC")
Student2=Student("Tessa","London")
#print("The name of the student is:",Student1.name,"and address is:",Student1.address)
#print("The name of the student is:",Student2.name,"and address is:",Student2.address)
print(Student1.getname()," ",Student1.getaddress())
print(Student2.getname()," ",Student2.getaddress())
