'''TYPES OF INHERITANCE
multiple inheritance->'''
class Car:
    def setengine(self,engine):
        self.engine=engine
    def getengine(self):
        return self.engine

class Tyre:
    def settyre(self,tyre):
        self.tyre=tyre
    def gettyre(self):
        return self.tyre

class Model(Car,Tyre):
    def setmodel(self,model):
        self.model=model
    def getmodel(self):
        return self.model

m1=Model()
m1.setengine("EK-1")
print(m1.getengine())

m1.settyre("Ceat")
print(m1.gettyre())

m1.setmodel("Honda")
print(m1.getmodel())

