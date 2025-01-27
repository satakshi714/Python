'''method overriding-->
it is closely related to inheritance when a child class method overwrite
the parent class method of the same name, paraemeters and return type but
provides it's own implemetation. This is known as method overwrite

Some pre-requisite for method overriding-->
1)inhertance is mandatory
2) method must have the same name as in the parent class( in parent class it
is called overridden)
3)The method must have the same number of parameters as in the parent class
'''
class Car:
    def setbrandname(self,brand):
        self.brand=brand
    def getbrandname(self):
        return self.brand

class Accord(Car):
    def setbrandname(self,brand):
        self.brand=brand
    def getbrandname(self):
        return self.brand
    def setmodel(self,model):
        self.model=model
    def getmodel(self):
        return self.model

a1=Accord()
a1.setbrandname("LOL")
print(a1.getbrandname())

a1.setmodel("FUNNY")
print(a1.getmodel())

