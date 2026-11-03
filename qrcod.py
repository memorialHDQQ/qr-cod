import qrcode

url = input("Введите URL: ")
img = qrcode.make(url)
img.save("qr.png")
print("QR-код сохранён в qr.png")