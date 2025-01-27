'''Method overloading means the ability to have multiple variables
with same name which vary in their parameters, it is the concept of
polymorphism. But python doesn't supporty this kind of overloading
(multiple methods with same name is not possible
In python we can create a method that can be called in different ways
This process of calling the same method in different ways is called
method overloading
Syntax:

'''
class Greeting:
    def sayHello(self,name=None,wish=None):
        if name is not None and wish is not None:
            print("Hello"+name+wish)
        elif name is not None and wish is None:
            print("Hello"+name)
        else:
            print("Hello")
greet=Greeting()

greet.sayHello()
greet.sayHello("Ram")
greet.sayHello("Ram","Good Morning")


