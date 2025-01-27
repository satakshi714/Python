"""wtp to find how mant times each character is repeated in a given string.
print each character in the string in sortted order with number of times it
is repeated
a=input("Enter string:")
l=[]
for i in a:
    if i not in l:
        l.append(i)
for i in sorted(l):
    c=0
    for j in a:
        if i==j:
            c+=1
    print(i,c)
"""
'''
wtp to check 2 strings are anagrams using sorted function
hint: two strings are said to be anagram if we can form one
string by arranging the charactes of another string
a=input("string1:")
b=input("string2:")
l1=sorted(a)
l2=sorted(b)
if l1==l2:
    print("anagrams")
else:
    print("not anagrams")
'''
a=input("string1:")
b=input("string2:")
if len(a)==len(b):
    l1=[]
    l2=[]
    for i in a:
        if i not in l1:
            l1.append(i)
    for i in b:
        if i not in l2:
            l2.append(i)
    c=0
    for i in l1:
        if i in l2:
            c+=1
    if c==len(l1):
        print("Anagrams")
    else:
        print("Not anagrams")
else:
    print("Not anagrams")
            
    
