a=['a','e','i','o','u','A','E','I','O','U']
b=0
for i in range(a,99):
    c=input("vowel or 9 to quit")
    while b<100:
        if c in a:
            print("vowel")
        elif (c==9):
            exit
        elif c not in a:
            print("not vowel")
            break
