'''
import re
txt="AThewww rain Spain"
x=re.search("^AThewww......*Spain$", txt)
if x:
    print("YES, There is a match")
else:
    print("No match")

'''
import re
s="hellohhh 12 hi 89 football. Howdy"
p="\d{2"
r=re.findter(p, s)
for i in r:
    print(a.gtoup())
