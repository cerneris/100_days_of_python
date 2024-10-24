# Password generator
import string
import random

def generate(password_length):
    content = string.ascii_letters + string.digits + string.punctuation
    password = [content[random.randint(0, len(content) - 1)] for i in range(password_length)]
    random.shuffle(password)
    password = "".join(password)
    return password

print("Welcome to the password generator!")
password_length = int(input("Please chooce password length: "))
password = generate(password_length)
print(f"Your generated password: {password}")