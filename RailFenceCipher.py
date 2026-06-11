def encrypt(text):
    even = text[::2]
    odd = text[1::2]
    return even + odd

def decrypt(cipher):
    n = len(cipher)
    mid = (n + 1)//2

    even = cipher[:mid]
    odd = cipher[mid:]

    result = ""

    for i in range(len(odd)):
        result += even[i] + odd[i]

    if len(even) > len(odd):
        result += even[-1]

    return result

msg = input("Message: ")

c = encrypt(msg)
print("Encrypted:", c)
print("Decrypted:", decrypt(c))