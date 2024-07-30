# Grouping with parentheses

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search('My number is 376-562-5150.')

print(match_object.group(1))

print(match_object.group(2))

print(match_object.group(0))

print(match_object.group())

print(match_object.groups())

areaCode, mainNumber = match_object.groups()
print(f'Area Code: {areaCode}, Main Number: {mainNumber}')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search('My phone number is (376) 562-5150.')
print(match_object.group(1))
print(match_object.group(2))

# Matching Multiple Groups with the pipe: |

heroRegex = re.compile(r'Batman|Iron Man')
match_object_1 = heroRegex.search('Batman and Iron Man.')
print(match_object_1.group())

match_object_2 = heroRegex.search('Iron Man and Batman.')
print(match_object_2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
match_object_3 = batRegex.search('Batmobile lost a wheel')
print(match_object_3.group())
print(match_object_3.group(1))
print(match_object_3.groups())


# Optional Matching with the Question Mark

batRegex = re.compile(r'Bat(wo)?man')
match_object_4 = batRegex.search('The Adventures of Batman!')
print(match_object_4.group())

match_object_5 = batRegex.search('Also... the Adventures of Batwoman :-)')
print(match_object_5.group())

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match_object_6 = phoneNumRegex.search('My number is 376-562-5150')
print(match_object_6.group())

match_object_7 = phoneNumRegex.search('My number is 562-5150')
print(match_object_7.group())

# Matching Zero or More with the Star

batRegex = re.compile(r'Bat(wo)*man')
match_object_8 = batRegex.search('The Adventures of Batman')
print(match_object_8.group())

match_object_9 = batRegex.search('The Adventures of Batwoman')
print(match_object_9.group())

match_object_10 = batRegex.search('The Adventures of Batwowowowowoman')
print(match_object_10.group())

# Matching One or More with the Plus

batRegex = re.compile(r'Bat(wo)+man')
match_object_11 = batRegex.search('The Adventures of Batwoman')
print(match_object_11.group())

match_object_12 = batRegex.search('The Adventures of Batwowowowowoman')
print(match_object_12.group())

match_object_13 = batRegex.search('The Adventures of Batman')
print(match_object_13 == None)

# Matching Specific Repetitions with Curly Brackets (fo){7}

# These two regular expressions match identical patterns:
# (Ha){3}
# (Ha)(Ha)(Ha)

# And these two regular expressions also match identical patterns:
# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r'(ha){3}')
match_object_14 = haRegex.search('hahaha')
print(match_object_14.group())

match_object_15 = haRegex.search('ha')
print(match_object_15 == None)
