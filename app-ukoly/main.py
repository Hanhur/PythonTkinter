from tkinter import *

# Okno ================================================================================================================
window = Tk()
window.title("Seznam úkolů")
window.minsize(400, 400)
window.resizable(False,False)

# Definujeme fonty a barvy ============================================================================================
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#e2cff4"
window.config(bg=main_color)

# Function ============================================================================================================
def add_text():
    # pridani text
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)

def remove_text_item():
    # odstrani jednu polozku seznamu
    list_box.delete(ANCHOR)

def clear_all_list():
    # odstrani vsechny polozky ze seznamu
    list_box.delete(0, END)

def save_tasks():
    # ulozit ukoly do textoveho souboru
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Error!!! soubor tasks.txt")


# Framy ===============================================================================================================
input_frame = Frame(window, bg=main_color)
input_frame.pack()

text_frame = Frame(window, bg=main_color)
text_frame.pack()

button_frame = Frame(window, bg=main_color)
button_frame.pack()

# Input frame - obsah =================================================================================================
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0, padx=5, pady=5)

add_button = Button(input_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color, command=add_text)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

# Scrollbar ==========================================================================================================
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S)

# Text frame - obsah ==================================================================================================
list_box = Listbox(text_frame, width=45, height=15, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

# Propojime scrollbar s list_boxem ====================================================================================
text_scrollbar.config(command=list_box.yview)

# Button frame - obsah ================================================================================================
remove_button = Button(button_frame, text="Odstranit", borderwidth=2, font=main_font, bg=button_color, command=remove_text_item)
remove_button.grid(row=0, column=0, padx=2, pady=10)

clear_button = Button(button_frame, text="Smazat", borderwidth=2, font=main_font, bg=button_color, command=clear_all_list)
clear_button.grid(row=0, column=1, padx=2, pady=10)

save_button = Button(button_frame, text="Ulozit", borderwidth=2, font=main_font, bg=button_color, command=save_tasks)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=8)

quit_button = Button(button_frame, text="Zavrit", borderwidth=2, font=main_font, bg=button_color, command=window.destroy)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=8)

# Vyukovou zonu =======================================================================================================
# north (s), south (j), east (v), west (z)
# test_label = Label(button_frame, text="testovaci", bg="red", fg="white")
# test_label.grid(row=1, column=0, sticky=W+E)

open_tasks()
# Cykl ================================================================================================================
window.mainloop()