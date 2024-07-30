import re

# Grouping with parentheses

print('\nGrouping with parentheses:\n')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search('My number is 376-562-5150.')
print(f'group(1): {match_object.group(1)}')
print(f'group(2): {match_object.group(2)}')
print(f'group(0): {match_object.group(0)}')
print(f'group(): {match_object.group()}')
print(f'groups(): {match_object.groups()}')
areaCode, mainNumber = match_object.groups()
print(f'Area Code: {areaCode}, Main Number: {mainNumber}')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
match_object = phoneNumRegex.search('My phone number is (376) 562-5150.')
print(f'group(1): {match_object.group(1)}')
print(f'group(2): {match_object.group(2)}')

# Matching Multiple Groups with the pipe: |

print('\nMatching Multiple Groups with the pipe: |\n')
heroRegex = re.compile(r'Batman|Iron Man')
match_object_1 = heroRegex.search('Batman and Iron Man.')
print(f'Searching: Batman and Iron Man. match_object_1.group(): {match_object_1.group()}')

match_object_2 = heroRegex.search('Iron Man and Batman.')
print(f'Searching: Irin Man and Batman. match_object_2.group(): {match_object_2.group()}')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
match_object_3 = batRegex.search('Batmobile lost a wheel')
print('Searching: Batmobile lost a wheel.')
print(f'match_object_3.group(): {match_object_3.group()}')
print(f'match_object_3.group(1): {match_object_3.group(1)}')
print(f'match_object_3.groups(): {match_object_3.groups()}')

# Optional Matching with the Question Mark ?

print('\nOptional Matching with the Question Mark ?:\n')
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

# Matching Zero or More with the Star *

print('\nMatching Zero or More with the Star *:\n')
batRegex = re.compile(r'Bat(wo)*man')
match_object_8 = batRegex.search('The Adventures of Batman')
print(match_object_8.group())
match_object_9 = batRegex.search('The Adventures of Batwoman')
print(match_object_9.group())
match_object_10 = batRegex.search('The Adventures of Batwowowowowoman')
print(match_object_10.group())

# Matching One or More with the Plus +

print('\nMatching One or More with the Plus +:\n')
batRegex = re.compile(r'Bat(wo)+man')
match_object_11 = batRegex.search('The Adventures of Batwoman')
print(match_object_11.group())

match_object_12 = batRegex.search('The Adventures of Batwowowowowoman')
print(match_object_12.group())

match_object_13 = batRegex.search('The Adventures of Batman')
print(match_object_13 == None)

# Matching Specific Repetitions with Curly Brackets (fo){7}

print('\nMatching Specific Repetitions with Curly Brackets (fo){7}:\n')
# These two regular expressions match identical patterns:
# (Ha){3}
# (Ha)(Ha)(Ha)

# And these two regular expressions also match identical patterns:
# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r'(ha){3}')
match_object_14 = haRegex.search('hahaha')
print(f'matching: hahaha in pattern (ha){{3}}, match_object_14.group(): {match_object_14.group()}')
match_object_15 = haRegex.search('ha')
print(f'matching: ha in patter (ha){{3}}, match_object_15 == None?: {match_object_15 == None}')

# Greedy and Nongreedy Matching

greedyHaRegex = re.compile(r'(Ha){3,5}')
match_object_16 = greedyHaRegex.search('HaHaHaHaHa')
print(match_object_16.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
match_object_17 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(match_object_17.group())

# THe findall() Method

phoneNumRegexAll = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
match_object_18 = phoneNumRegex.search('Personal NUmber: 415-555-9999 Work Number: 212-555-0000')
print(match_object_18.group())
match_object_19 = phoneNumRegexAll.findall('Personal NUmber: 415-555-9999 Work Number: 212-555-0000')
print(match_object_19) # tuple

phoneNumRegexAllGroups = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
match_object_20 = phoneNumRegexAllGroups.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(match_object_20)
