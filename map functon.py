globvar="Hello"
def test1():
    global globvar
    golbvar="Good Morning"

def test2():
    globvar="Night Night"

print(globvar)
test1()
