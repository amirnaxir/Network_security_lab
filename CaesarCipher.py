def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = input("Message: ")
s = int(input("Shift: "))

cipher = encrypt(msg, s)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, s))