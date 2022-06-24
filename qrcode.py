import pyqrcode
link = "www.instagram.com/mr.programmer78"
qrcode = pyqrcode.create(link)
qrcode.png("output.png", scale=8, module_color='FF00FF', background='FFC0C0')

# http://www.simotime.com/sim4clrs.htm
