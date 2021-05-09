import pyqrcode

data = input("Enter the Link For which you want to make QR Code...")


image = pyqrcode.create(data)

image.png("pyqrcode.png",scale=8)

