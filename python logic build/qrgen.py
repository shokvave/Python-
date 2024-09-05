#install all the libraries needed
#create a function that collects the text and converts into   qr code
# save the qr code 

import   qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
 
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "Black", back_color = "White" )
    img.save("qrimg001.png ")

url = input("ENter the url: ")

generate_qrcode(url)
