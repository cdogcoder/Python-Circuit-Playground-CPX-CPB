import re

from_count = 0
to_count = 0
email_count = 0
xfile = open('text-file-mail-short.txt')
all_emails_with_date = re.findall(r"\w\w\w, \d\d \w\w\w \d\d\d\d \d\d:\d\d:\d\d", xfile.read())
oldest_date = all_emails_with_date[-1]

xfile = open('text-file-mail-short.txt')
for line in xfile:
    if line[:5] == "From:":
        from_count += 1
        print("From count: ", from_count, line)
    elif line[:3] == "To:":
        to_count += 1
        print("To count: ", to_count, line)
    elif "@" in line:
        email_count += 1
        print("Email count: ", email_count, line)
    elif oldest_date in line:
        print("THE OLDEST EMAIL GUYS: ", line)

    print(line, end="")
