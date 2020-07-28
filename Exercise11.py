#Email Collector
import re
string = '''aniket
aniket111awa@gmail.com 
ankita 
ankita123@gmail.com 
aakash 
aakash234@gmail.com 
anant 
anant234@gmail.com'''
# patt = re.compile(r'@gmail.com$')
# emails = patt\
#     .finditer(string)
# for email in emails:
#     print (email,"\n")
#     print(string[104:114])

# email = re.findall(r'[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+',string)
# \w -> all characters from atoz and AtoZ and special cjaracter
# \S -> no white space afte @
email = re.findall(r'\w+@\S+\w',string)
print(email)