from tkinter import *
import psycopg2 

root = Tk()
root.title('Vypocet BMI')
root.geometry('350x350')
root.resizable(False, False)

# general label ================================================================
label_general = Label(root, text = 'Vypocet BMi')
label_general.grid(row = 0, column = 1)

# weight section ===============================================================
label_weight = Label(root, text = 'Zadejte vahu (kg): ')
label_weight.grid(row = 1, column = 0)

entry_weight = Entry(root)
entry_weight.grid(row = 1, column = 1)

# height section ===============================================================
label_height = Label(root, text = 'Zadejte vysku (m): ')
label_height.grid(row = 2, column = 0)

entry_height = Entry(root)
entry_height.grid(row = 2, column = 1)

# Button =======================================================================
button = Button(root, text = 'Vypocitat')
button.grid(row = 3, column = 1)


root.mainloop()