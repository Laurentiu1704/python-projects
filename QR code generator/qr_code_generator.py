import qrcode

filename = input("Enter file name: ").strip()
searchdata = input("Enter the query: ").strip()

img = qrcode.make(searchdata)
type(img)  # qrcode.image.pil.PilImage
img.save(filename + ".png")