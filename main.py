import qrcode as qr
from PIL import Image

data = input("QR: ")

img = qr.make(data)
img.save("qr.png");

im = Image.open("qr.png")
im.show();
