import re

# Ask about the key (remember the edge cases)

while True:
    key = input("What should be the key? ")
    if key.isdigit() and int(key) > 0:
        # Use modulo 26 in case user give key greater than 26
        key = int(key) % 26
        break
    else:
        print("You have to give a number (above zero).")

# Ask about the plain text (remember the edge cases)

while True:
    plain_text = input("What text do you want to be enciphered? ").lower()
    if re.search("[a-z]", plain_text):
        break
    else:
        print("You have to write at least one character of English alphabet.")

# Take each character (only letter) and change it using the key

cipher_text = ""
for char in plain_text:
    cipher_num = ord(char) + key
    if char in "abcdefghijklmnopqrstuvwxyz" and cipher_num < 122:
        cipher_text += chr(cipher_num)
    elif char in "abcdefghijklmnopqrstuvwxyz" and cipher_num > 122:
        cipher_text += chr(ord("`") + (cipher_num % ord("z")))
    else:
        cipher_text += char

# Return enciphered text

print(f"The enciphered text is '{cipher_text}'.")