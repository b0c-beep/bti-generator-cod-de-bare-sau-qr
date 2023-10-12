#Importam librariile necesare pentru generarea codurilor de bare si QR
import qrcode as qr
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter

#Verificam decizia utilizatorului
choice = input("Cod de bare (1) sau QR (2)?") 

#Executam cazul codului QR
if choice == "2":
    data = input("QR: ") #Salvam continutul viitorului cod QR

    img = qr.make(data) #Transformam continutul in imagine
    img.save("qr.png");

    im = Image.open("qr.png")
    im.show(); #Afisam imaginea

#Executam cazul codului de bare
elif choice == "1":
    number = input("Numar (12 cifre): ") #Salvam continutul viitorului cod de bare

    code = EAN13(number, writer = ImageWriter()) #Codificam informatia folosind libraria necesara
    code.save("barcode")

    im = Image.open("barcode.png") 
    im.show() #Afisam imaginea

#Sfarsitul programului
