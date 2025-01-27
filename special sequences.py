'''
.(Period)- This matches any single character except newline
^(Caret)- This is used to check if a string starts with a certain character
$(Dollar)- This is used to check if a string ends with a certain character
+(Plus)- This matches one or more occurances of the pattern left to it
*(Star)- This matches zero or more occurances of the pattern left to it
?(Question mark)_ This maytches zero or one occurances of the pattern lest to it
{n,m}(Braces)-This means atleast n, and at most m repetetion of the pattern left
to it.
|(Alternation)- THis vertical bar is used for alternation(or operator)
()(Group)- This is used to group sub-patterns
\(Backslash)-This is ude to escape various characters including all meta
characters
___________________________________
Special Sequences--
\A- This matches the Specified characters are at the start of the string
\b- This matches if the specified charscters are at the begenining or end
of the word
\B- Opposite of \b. This matches if the specified characters are not at
the begenimg or end of the word
\d- This matches any decimal digit.Equivalent[0 to 9]
\D- This matches any non-decimal digits.Equivakent to[^0 to 9]
\s- This matches where a string contains any whitespace characters
\S- This matches where a string contains any non-ehitespace characters
\w- This matches any alphanumeric character which is equivalent to [a-zA-0-9_]
\W- This matches any non-alphanumeric character.
\Z- This matches if the specified characters are at the end of the string
_________________________________________
Pattern methods-pattern objects have several methods and attributes which
are used
match()- It tries to find the regular expression match at the beginning of
the match
search()- It tries to find the RE match at any location
findall()- It finds all the substrings of the RE where if matches and returns
them as the list
finditer()- It finds all the substrings of the RE where if matches and
returns them as an iterator
'''
"""
import re
p='^a...s%'
test="abyss"
print(result)
result=re.match(p,test)
print(result.group())
print(result.start())
print(result.end())
print(result.span())
if result:
    print("search Succesful")
else:
    print("Search unsuccessful")
"""
'''Thse match if found will return a match object which can be used later.
This match object has many methods -
group()- This return the string matched by thr RE
start()- This returns thr=e starting position if the match
end()- This returns the ending posiion of the match
span()- This returns a tuple containing the (start,end) positions of the match
This method works for both match() and search()
'''
import re
s="hellojen1 mvo0303.vkiji409 49"
p='\d+'
result=re.findall(p,s)
print =(result)
