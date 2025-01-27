a=input("data1: ").split(",")
b=input("data2: ").split(",")
c=input("data3: ").split(",")
for i in range(0,len(a)):
    b[i]=int(b[i])
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,len(c)):
    c[i]=int(c[i])
mat=[a,b,c]
print(mat)
rows=len(mat)
cols=len(mat[0])
size=rows*cols
c=0
for i in range(rows):
    for  j in range(cols):
        if (mat[i][j]==0):
            c+=1
if c>(size/2):
    print("Sparse Matrix")
else:
    print("Not a sparse Matrix")
