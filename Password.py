from random import choice
import string

def rand_password(length):
    char = string.ascii_letters + string.digits
    password = ''.join(choice(char) for i in range(length))
    return password
print("Enter the length of the password required:")
length1 = int(input(""))
password = rand_password(length1)
print("Generating Random Password:", password)