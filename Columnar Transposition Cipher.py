plain = input("Enter Plain Text: ").upper()

if len(plain) % 2 != 0:
    plain += "X"

cipher = ""

for i in range(0, len(plain), 2):
    cipher += plain[i+1]
    cipher += plain[i]

print("Cipher Text:", cipher)
