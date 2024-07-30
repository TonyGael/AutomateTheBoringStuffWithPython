import re

# Finding Patters of Text with Regular Expressions
# Regular expressions, called regexes for short, are descriptions for a
# ­pattern of text. For example, a \d in a regex stands for a digit character—
# that is, any single numeral 0 to 9. The regex \d\d\d-\d\d\d-\d\d\d\d is used
# by Python to match the same text the previous isPhoneNumber() function did:
# a string of three numbers, a hyphen, three more numbers, another hyphen,
# and four numbers. Any other string would not match the \d\d\d-\d\d\d-\d\d\d\d regex.

# But regular expressions can be much more sophisticated. For example,
# adding a 3 in curly brackets ({3}) after a pattern is like saying, “Match this
# pattern three times.” So the slightly shorter regex \d{3}-\d{3}-\d{4} also
# matches the correct phone number format.

# creating a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # r from raw string

# Matching Regex Objects
match_object = phoneNumRegex.search('My number is 376-562-5150')  # search() is a method from Regex Object'ss
print(f'Phone number found: {match_object.group()}')  # Match Object's group() method
