def rail_fence_encrypt(text):
    even = ""
    odd = ""

    for i in range(len(text)):
        if i % 2 == 0:
            even += text[i]
        else:
            odd += text[i]

    return even + odd

plain = input("Enter Plain Text: ").upper()

cipher = rail_fence_encrypt(plain)

print("Cipher Text:", cipher)
