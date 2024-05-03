from tkinter import *

window = Tk()
window.title("Převod měn c CZK na EUR")
window.minsize(200, 200)
window.resizable(False, False)
window.config(bg="#061856")

# 1 euro = 25.00
# Function
def count_corrency():
    amount_eur = float(amount_input.get()) / 25.00
    result_label["text"] = round(amount_eur, 2)

# Vstup od uzivatela
amount_input = Entry(width=10, font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)

# Label
czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#061856", fg="white")
czk_label.grid(row=0, column=1)

eur_label = Label(text="EUR", font=("Helvetica", 15), bg="#061856", fg="white")
eur_label.grid(row=1, column=1)

result_label = Label(text="0", font=("Helvetica", 15), bg="#061856", fg="white")
result_label.grid(row=1, column=0)

# Button
count_button = Button(text="Převést", font=("Helvetica", 15), command=count_corrency)
count_button.grid(row=0, column=2, padx=10, pady=10)

window.mainloop()