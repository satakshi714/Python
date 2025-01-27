class Abs():
    def f1():
        raise NotImplementedError("need overriding")

class Derived(Abs):
    def f2():
        print("Hello")

d1=Derived
d1.f1()
a1=Abs
a1.f1()
