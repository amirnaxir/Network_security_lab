def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ key)
    return result

msg = input("Message: ")
key = 5

cipher = encrypt(msg, key)

print("Encrypted:", cipher)
print("Decrypted:", encrypt(cipher, key))