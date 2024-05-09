from tkinter import *
import psycopg2 

root = Tk()
root.title('Vypocet BMI')
root.geometry('300x300')
root.resizable(False, False)

# general label ================================================================
label_general = Label(root, text = 'Vypocet BMi')
label_general.grid(row = 0, column = 1)

# weight section ===============================================================
label_weight = Label(root, text = 'Zadejte vahu (kg):')
label_weight.grid(row = 1, column = 0)

entry_weight = Entry(root)
entry_weight.grid(row = 1, column = 1)

# height section ===============================================================
label_height = Label(root, text = 'Zadejte vysku (m):')
label_height.grid(row = 2, column = 0)

entry_height = Entry(root)
entry_height.grid(row = 2, column = 1)

# Button =======================================================================
button = Button(root, text = 'Vypocitat')
button.grid(row = 3, column = 1)

# result section ==============================================================
label_result_1 = Label(root, text = 'Ciselny vysledek:')
label_result_1.grid(row = 4, column = 0)

label_user_result_1 = Label(root, text = 'DOPLNIT')
label_user_result_1.grid(row = 4, column = 1)

label_result_2 = Label(root, text = 'Textovy vysledek:')
label_result_2.grid(row = 5, column = 0)

label_user_result_2 = Label(root, text = 'DOPLNIT')
label_user_result_2.grid(row = 5, column = 1)

label_count_text = Label(root, text = 'Pocet uzivatelu:')
label_count_text.grid(row = 6, column = 0)

label_count_number = Label(root, text = 'DOPLNIT')
label_count_number.grid(row = 6, column = 1)

root.mainloop()