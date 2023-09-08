import segno

qrcode = segno.make_qr("Hello World")

qrcode.save(
    "qrcode.png",
    scale=5
)
