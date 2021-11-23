import shutil
import  re
from faker import Faker

fake = Faker('en_US')

with open('potential-contacts.txt', 'r') as f:
    text = f.read().replace('\n', '')

phone_regex = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)

email_regex = re.compile(r'''([a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

phone = []
email = []

for i in phone_regex.findall(text):
    phone_num = '-'.join([i[1], i[3], i[5]])
    phone_num = re.sub(r'[(|)]','', phone_num)
    if phone_num not in phone:
        phone.append(phone_num)
for i in email_regex.findall(text):
    if i[0] not in email:
        email.append(i[0])

phone.sort()
email.sort()
"""
#.Create The File
with open('phone_numbers.txt','w') as f:
    for element in phones:
     f.write(element + "\n")
#.Move The File
shutil .move('phone_numbers.txt', 'assest')

#.Create The File
with open('emails.txt', 'w') as f:
    for element in emails:
     f.write(element + "\n")
#.Move The File
shutil .move('emails.txt', 'assest')
"""
print(len(phone))
print(str(phone))
print("-" * 50)
print(len(email))
print(str(email))