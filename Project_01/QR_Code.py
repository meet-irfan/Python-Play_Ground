import qrcode
import qrcode as gr
img = qrcode.make("https://www.linkedin.com/feed/")
img.save("linkedin.png")