import qrcode as qr
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter

choice = input("Cod de bare (1) sau QR (2)?")

if choice == "2":
    data = input("QR: ")

    img = qr.make(data)
    img.save("qr.png");

    im = Image.open("qr.png")
    im.show();


elif choice == "1":
    number = input("Numar (12 cifre): ")

    code = EAN13(number, writer = ImageWriter())
    code.save("barcode")

    im = Image.open("barcode.png")
    im.show()
