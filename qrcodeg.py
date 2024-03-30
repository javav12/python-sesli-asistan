import qrcode
import os
ky = False






qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)
def kontrol():
    ky = False
    if  "qrcodes" not in os.listdir():
        ky = True
    if ky == True:
        os.mkdir("qrcodes")

def mkqr(data):
    kontrol()
    qrs = len(os.listdir("qrcodes"))
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcodes/QR({}).png".format(qrs))
