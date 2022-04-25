from idna import valid_string_length
import qrcode
from PIL import Image
from cv2 import cv2
print('Enter information to encode')
site=input()
features = qrcode.QRCode(version=1, box_size=40, border=3)
features.add_data(site)
features.make(fit=True)
qr = features.make_image(fill_color="black", background_color="white")
qr.save('image2.png')

img = cv2.imread('image2.png')
d = cv2.QRCodeDetector()
val, b ,c = d.detectAndDecode(img)
print(val)
