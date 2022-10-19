import pyqrcode
import png
from pyqrcode import QRCode

s = "Uday Sankar Mukherjee  123456789  Btech 1st year CSE(AI ML) IC 12021002016057"

url =  pyqrcode.create(s)
url.svg("myqr.svg" , scale = 8)
url.png('myqr.png' , scale = 6)



