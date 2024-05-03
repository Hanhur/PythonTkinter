import requests
from tkinter import *

# Okno
window = Tk()
window.minsize(700, 400)
window.resizable(False, False)
window.title("ISS")

# Fanction
def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    latitude_labal.config(text=f"Zemepisna sirka ISS je: {latitude}")
    longitude_label.config(text=f"Zemepisna delka ISS je: {longitude}")

# Canavs
canvas = Canvas(window, width=500, height=280)
canvas.pack()
iss_img = PhotoImage(file="img/iss.gif")
canvas.create_image(0, 0, anchor="nw", image=iss_img)

# Framy
coordinates_frame = Frame(window)
coordinates_frame.pack()

# Button
recount_button = Button(coordinates_frame, text="Positions ISS", command=iss_coordinates)
recount_button.pack()

# Labels
latitude_labal = Label()
latitude_labal.pack()

longitude_label = Label()
longitude_label.pack()

window.mainloop()
