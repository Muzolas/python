"""
Parola oluşturan bir program.

string.digits: 0123456789
string.punctuation: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
string.ascii_letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
"""

import random
import string

def generate_password(length, level, output=[]): # şifre oluşturma fonksiyonu 

    chars = string.ascii_letters  # ascii harflerini aldığımız yer

    if level > 1:
        chars = "{}{}".format(chars, string.digits)  # sayılar

    if level > 2:
        chars = "{}{}".format(chars, string.punctuation) # işaretler
    
    for i in range(length):
        output.append(random.choice(chars)) # rastgele alınan değerler
    
    return "".join(output)

print(("-" * 30) + "\n Password Generator\n" + ("-" * 30))

password_length = int(input("Length: "))
password_level = int(input("Level: "))

password = generate_password(password_length, password_level)
print("\nYour password is: {}".format(password))
