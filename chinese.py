x = 1

while True:
    if x % 3 == 2 and x % 5 == 3 and x % 7 == 2:
        print("Solution =", x)
        break
    x += 1