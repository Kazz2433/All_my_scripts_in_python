#! python 3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneregex = re.compile(r'''(
    [+]?
    (\d)?
    (\s|-|\.)?
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)                     # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                     # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''',re.VERBOSE)

# Create email regex
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-somethin
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches=[]
for groups in phoneregex.findall(text):
    matches.append(groups[0])
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addres found')