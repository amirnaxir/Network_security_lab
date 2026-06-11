def aes_encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

msg = input("Message: ")
key = 7

cipher = aes_encrypt(msg, key)

print("Encrypted:", cipher)
print("Decrypted:", aes_encrypt(cipher, key))