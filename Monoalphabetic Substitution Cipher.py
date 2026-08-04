alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

plain = input("Enter Plain Text: ").upper()

cipher = ""

for ch in plain:
    if ch in alphabet:
        cipher += key[alphabet.index(ch)]
    else:
        cipher += ch

print("Cipher Text:", cipher)