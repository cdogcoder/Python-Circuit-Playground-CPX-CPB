import re

xfile = open('text-file-mail-short.txt')
all_emails = re.findall(r"[a-zA-Z0-9.]+@[a-zA-Z0-9.]+", xfile.read())
for i in all_emails:
    print(i)
