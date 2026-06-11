a = int(input("Enter a: "))
p = int(input("Enter prime p: "))

result = pow(a, p-1, p)

if result == 1:
    print("Fermat theorem verified")
else:
    print("Not verified")

print("Result =", result)