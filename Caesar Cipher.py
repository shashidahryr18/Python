def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result

text = input("Enter Plain Text: ")
shift = int(input("Enter Key: "))

cipher = encrypt(text, shift)

print("Cipher Text:", cipher)
