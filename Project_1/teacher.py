from tkinter import * 
import psycopg2 

root = Tk()
root.title('Skola a databaze')
root.geometry('350x280')
root.resizable(False, False)

# Functions ==================================================================
def insert_data(name, age, address):
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_address.delete(0, END)

    connection = psycopg2.connect(
        dbname = 'student',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    cursor = connection.cursor()
    query = '''INSERT INTO teacher(name, age, address) VALUES (%s, %s, %s)'''
    cursor.execute(query, (name, age, address))

    connection.commit()
    connection.close()
    display_all()

def search(id):
    connection = psycopg2.connect(
        dbname = 'student',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    cursor = connection.cursor()
    query = '''SELECT * FROM teacher WHERE id = %s'''
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    if row:
        display_search(row)
    else:
        display_search('ID nenalezeno')

    connection.commit()
    connection.close()

def display_search(data):
    listbox = Listbox(root, width = 20, height = 1)
    listbox.grid(row = 8, column = 1)
    listbox.insert(0, data)

def display_all():
    connection = psycopg2.connect(
        dbname = 'student',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    cursor = connection.cursor()
    query = '''SELECT * FROM teacher'''
    cursor.execute(query)
    all_data = cursor.fetchall()
    listbox = Listbox(root, width = 25, height = 5)
    listbox.grid(row = 9, column = 1)
    for one_row in all_data:
        listbox.insert(0, one_row)

display_all()

label_general = Label(root, text = 'Add data')
label_general.grid(row = 0, column = 1)

# Name ==================================================
label_name = Label(root, text = 'Name: ')
label_name.grid(row = 1, column = 0)

entry_name = Entry(root)
entry_name.grid(row = 1, column = 1)

# Age ===================================================
label_age = Label(root, text = 'Age: ')
label_age.grid(row = 2, column = 0)

entry_age = Entry(root)
entry_age.grid(row = 2, column = 1)

# Address ================================================
label_address = Label(root, text = 'Address: ')
label_address.grid(row = 3, column = 0)

entry_address = Entry(root)
entry_address.grid(row = 3, column = 1)

# Button =================================================
button = Button(root, text = 'Add', command = lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row = 4, column = 1)

# Serch Section ==========================================
label_rearch = Label(root, text = 'Search data')
label_rearch.grid(row = 5, column = 1)

# ID section =============================================
label_id = Label(root, text = 'search by ID: ')
label_id.grid(row = 6, column = 0)

entry_id = Entry(root)
entry_id.grid(row = 6, column = 1)

# Button Search ==========================================
button_search = Button(root, text = 'Search', command = lambda:search(entry_id.get()) if entry_id.get().strip() else None)
button_search.grid(row = 6, column = 2)

# Cyclus =================================================
root.mainloop()