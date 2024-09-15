import re

txt = '''
abcdefghijklmnopqrstqpwxyz
ABHCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Matecharacters (need to be escaped)

. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321--555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
pat 
bat

emails:

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''

s  = 'Start a sentence and then bring it to an end'

# Pattern to find phone numbers
pattern = re.compile(r'[A-Za-z0-9._%+-]*\@[A-Za-z0-9.-]*\.[A-Za-z]{2,}')


#HTTP URLs : (r'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

#Email ID: (r'[A-Za-z0-9._%+-]*\@[A-Za-z0-9.-]*\.[A-Za-z]{2,}')



matches = pattern.finditer(txt)


for match in matches:
  print(match)
  
'''

#for match in matches:
print(matches)


with open ('test_copy.txt', 'r', encoding = 'utf-8') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

for match in matches:
  print(match)'''

# Example output:
# 321-555-4321
# 123.555.1234




'''

.            - Any Char Except New Line
\d           - Digit (0 - 9)
\D           - Not A Digit (0 - 9)
\w           - Word Char (a - z, A - Z, 0 - 9)
\W           - Not A Word Char
\s           - Whitespace (space, tab, newline)
\S           - Not Whitespace (space, tab, newline)
\b           - Word Boundary
\B           - Not A Word Boundary
^            - Beginning Of A String
$            - End Of A String
[]           - Matches Char In Brackets
[^ ]         - Matches Char Not In

Quantifiers:

*            - 0 or more
+            - 1 or more
?            - 0 or One
{3}          - Exact Number
{3, 4}       - Range of Numbers (Minimum, Maximum)



###### SAMPLE REGEX ######

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.

'''
