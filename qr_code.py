import qrcode 
from PIL import Image
qr=qrcode.QRCode(version=8,box_size=10,border=4)
qr.add_data(input("enter link to generate QR Code:\n"))
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save("QRcode.png")

print("QR Code generated Successfully")