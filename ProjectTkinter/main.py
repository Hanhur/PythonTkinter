from tkinter import *

# Okno
window = Tk()
window.title("Change")
window.minsize(width=500, height=500)
window.resizable(False, False)
window.iconphoto(False, PhotoImage(file="icons/icon.png"))
window.config(bg="#0c1f62")

# Label
greet_label = Label(window, text="EUR", bg="black", fg="white", font=("Helvetica", 18, "bold"), borderwidth=5, relief="sunken")
greet_label.pack(pady=50)

greet_label = Label(window, text="CZK", bg="black", fg="white", font=("Helvetica", 18, "bold"), borderwidth=5, relief="sunken")
greet_label.pack()

def change_text():
    greet_label["text"] = input_1.get()
    greet_label["text"] = text_field.get("1.0", END)
    input_1.delete(0, END)

button_1 = Button(text="Click", command = change_text)
button_1.pack()

input_1 = Entry(width = 20, font=("Helvetica", 18, "bold"))
input_1.insert(0, string="Mango")
input_1.focus()
input_1.pack()


text_field = Text(width=40, height=10)
text_field.focus()
text_field.pack()



# Hlavní cyklus
window.mainloop()

# 12
