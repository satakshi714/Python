'''FIle Handling
In python file operation takes place in the following order
1) open the file- To oper the file we use a built in open function which has
two arguments: file name, mode.
Syntax: file_object= open(filename, mode)

2) read or write operation

3) close the file

Binary files vs text files:
Following Modes for opening, reading or writing text files:
1) Read mode(default mode)-'r'
2) Write mode(overwrite)='w'
3) Append(add at last)='a'
4) exclusive creationg( it opens a file for exclusive creation,
if the file already exist the operation fails)-'x'
5) Read or write mode 'r+'
6) Append or readmode-'a+'

Modes while using binary files
1) wb
2) rb
3) ab
4) rb+
5) ab+
'''

"""Read method
file= open("file.txt","r")
print(file.read())
"""

''' Read line (this will read one line and append a newline character/n
Strip- it will strip the extra lines
file= open("file.txt","r")
for i in range(4):
    print(file.readline().strip())
'''

"""Read lines- This method reads file line by line into a list
file= open("file.txt","r")
print(file.readlines())
"""
'''Write method - It is used to write a string into a file, it
only accepts the string as an argument
file= open("abc.txt","r+")
file.write("File handling")
file.seek(23)       # it will change the position of cursor
print(file.read())
file.close()
print(file.tell())  #it will tell theposition of cursor
'''

"""Write lines- User writes a list of strings into a file.
It accepts both strings and list as an argument

file=open("abc.txt","r+")
l1=["first class\n","second class\n","third class\n"]
file.writelines(l1)
file.seek(0)
print(file.read())
print(file.tell())
print(file.close())
"""
'''Q Write a program to print each line in reverse order?

file= open("abc.txt","r+")
for i in file:
    print(i[::-1].strip())
'''
"""
Q) wtp to print the number of lines, words and characters in the file"""




