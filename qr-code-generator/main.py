import pyqrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Generator QR kodu')
root.geometry('300x300')
root.resizable(False, False)

# Globalni promennou
global_photo_image = None

# Functions
def generate_qr_code():
    global global_photo_image
    qr = pyqrcode.create(url_entry.get())
    qr.png('qr_code.png', scale = 5)

    image = Image.open('qr_code.png')
    global_photo_image = ImageTk.PhotoImage(image)

    label = Label(root, image = global_photo_image)
    label.pack()

url_label = Label(root, text = 'Zadajte URL adressu')
url_label.pack(pady = (10, 5))

url_entry = Entry(root, width = 30)
url_entry.pack(pady = (0, 20))

button = Button(text = 'Vygenerovat QR kod', command = generate_qr_code)
button.pack()


root.mainloop()