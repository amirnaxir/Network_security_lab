def rc4(text, key):
    result = ""

    for i in range(len(text)):
        k = ord(key[i % len(key)])
        result += chr(ord(text[i]) ^ k)

    return result

msg = input("Message: ")
key = input("Key: ")

cipher = rc4(msg, key)

print("Encrypted:", cipher)
print("Decrypted:", rc4(cipher, key))