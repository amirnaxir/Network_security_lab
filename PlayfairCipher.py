def playfair_encrypt(text):
    text = text.replace(" ", "").upper()
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        result += text[i+1] + text[i]
    return result

def playfair_decrypt(text):
    return playfair_encrypt(text)

msg = input("Message: ")

cipher = playfair_encrypt(msg)
print("Encrypted:", cipher)
print("Decrypted:", playfair_decrypt(cipher))