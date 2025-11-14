###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if 'a' <= char <= 'z':
        # small letter: shift and wrap around
        new_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        # capital letter: shift and wrap around
        new_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        # non-letter: keep unchanged
        new_char = char
    encrypted_text += new_char

print('Original:', plain_text)
print('Encrypted:', encrypted_text)