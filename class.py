class Student:
    def __init__(self,name,address):
        self.name=name
        self.address=address
Student1=Student("Izzy","NYC")
Student2=Student("Tessa","London")
print("The name of the student is:",Student1.name,"and address is:",Student1.address)
print("The name of the student is:",Student2.name,"and address is:",Student2.address)
