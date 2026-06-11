import numpy as np

key = np.array([[3, 3],
                [2, 5]])

msg = input("Enter 2 letters: ").upper()

p = [ord(msg[0])-65, ord(msg[1])-65]

cipher = np.dot(key, p) % 26

enc = ''.join(chr(int(x)+65) for x in cipher)

print("Encrypted:", enc)