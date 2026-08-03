import qrcode

text = input("https://github.com/shashidahryr18")

qr = qrcode.make(text)

filename = "qrcode.png"

qr.save(filename)

print("QR Code saved as", filename)
