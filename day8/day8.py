# Ceasars cypher
import string

UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase

def encrypt(_str, jump_num):
    new_str = ""
    for i in range(len(_str)):
        if _str[i].isupper():
            cur_index = UPPER.index(_str[i])
            new_str += UPPER[(cur_index + jump_num) % len(UPPER)]
        elif _str[i].islower():
            cur_index = LOWER.index(_str[i])
            new_str += LOWER[(cur_index + jump_num) % len(LOWER)]
        else:
            new_str += _str[i]
    print(new_str)
    return new_str

def decrypt(_str, jump_num):
    new_str = ""
    for i in range(len(_str)):
        if _str[i].isupper():
            cur_index = UPPER.index(_str[i])
            new_str += UPPER[(cur_index - jump_num) % len(UPPER)]
        elif _str[i].islower():
            cur_index = LOWER.index(_str[i])
            new_str += LOWER[(cur_index - jump_num) % len(LOWER)]
        else:
            new_str += _str[i]
    print(new_str)
    return new_str

print("Welcome to Caesar's Cypher!!")
jump_num = int(input("Please enter the number to jump: "))
_str = input("Please enter string to encrypt: ")
print("Encrypted string:")
encrypted = encrypt(_str, jump_num)
print("Decrpyted string (ORIGINAL): ")
decrypted = decrypt(encrypted, jump_num)