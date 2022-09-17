def encrypt(text, value, output=""): # Şifreleme

    for char in text:
        output = "{}{}".format(output, chr(ord(char) + value))

    return output

def decrypt(text, value, output=""): # Çözümleme

    for char in text:
        output = "{}{}".format(output, chr(ord(char) - value))

    return output

i = int(input("Increment value: "))

text = input("Type your text: ")

print("Encrypted text: {}".format(encrypt(text, i)))

text = input("\nType for decrypt: ")

print("Decrypted text: {}".format(decrypt(text, i)))
