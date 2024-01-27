import pandas as pd
import qrcode

# Read data from xlsx file and convert it to dictionary
file_name = "Stars cards.xlsx"

df = pd.read_excel(file_name, sheet_name='Stars Cards')
dict = pd.Series(df.Kid_name_english.values, index=df.Kid_Id).to_dict()
print(dict)

# Create QR code for each kid

path = "qr\\"

for key, value in dict.items():
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    data = key
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(1, 48, 71), back_color="transparent")
    img.save(path + value + ".png")
