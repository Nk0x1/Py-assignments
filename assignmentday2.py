

#1-mail verification
"""
import re
m=str(input('Enter your mail ID: '))
p="[a-zA-Z0-9]+\@[gmail|^yh]+\.[org|com|in]+"
if re.findall(pattern,m)==[]:
    print('Invalid Mail')
else: 
    print(re.findall(pattern,m))
"""
#2-Phone number verification
"""
import re
phn=(input('Enter a phone number: '))
p="^\(\d{3}\)-\d{3}-\d{4}$"
if re.findall(p,phn)!=[]:
    print('The number is valid')
     
else:
    print("invalid format,checking for country code")
    c="\+\d{2}\(\d{3}\)-\d{3}-\d{4}$"
    if re.findall(c,phn)!=[]:
        print(re.findall(p,phn))
        print('it is a valid number')
    else:
        print("This phone number is not valid") 
"""
#3-domain from URL
"""
import re
url=input("Enter a URL: ")
p=r'^https?://(www\.)?([a-zA-Z0-9.-]+).*'
chk=re.match(p, url)
if chk:
    d = chk.group(2)
    print(f"Domain= {d}")
else:
    print("Invalid URL")
       
"""
#4-Date format
"""
import re
date= input("Enter a date (MM/DD/YYYY): ")
p = r'(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})'
chk = re.findall(p, date)
if chk:
        print("Found date in the format: ", date)
else:
    print("Invalid,Date not found")    
"""

#5-HTML tags
"""
import re
p = r'<[^>]*>'
s= input("Enter string with HTML tags: ")
nohtml = re.sub(p, '', s)
print("String: ")
print(nohtml)
"""

#6-IP address
"""
import re
p = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
ip=input("Enter ip address: ")
chk = re.findall(p, ip)
if chk:
        print("Valid=", ip)
else:
    print("Invalid.")
"""

#7-Password 
"""
import re
p = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
pw = input("Enter password: ")
if re.match(p, pw):
    print("Valid=",pw)
else:
    print("Invalid")
"""

#8-hashtags
"""
import re
p = input("Enter a social media post: ")
h = re.findall(r'#\w+',p)
if h:
    print("The hastags: ")
    for i in h:
        print(i)
else:
    print("Not found")
"""

#9-URL
"""
import re
text = input("Enter text: ")
p = r'https?://\S+|www\.\S+'
url = re.findall(p, text)
if url:
    print("Found URLs:")
    for i in url:
        print(i)
else:
    print("URLs not found")
"""

#10-numbers
"""
import re
text = input("Enter text: ")
p = r'\d+'
n = re.findall(p, text)
if n:
    print("Numbers Found:")
    for i in n:
        print(i)
else:
    print("Not found")
    
"""


    




