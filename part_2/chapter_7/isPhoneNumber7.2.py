def isPhoneNumber(text):

    if len(text) != 12:
        return False
        
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False
        
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
            
    return True

message = 'Call me at 376-462-5150 tomorrow. 3765-462-5150 es my office.'
count = 0

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f'Phone number found: {chunk}')
        count += 1
    
print(f'Done!\nNumber found {count} times.')

print('n times Chunk would be:')
for i in range(len(message)):
    chunk = message[i:i+12]
    print(f'{i} chunk : {chunk}')
