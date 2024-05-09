from tkinter import *
import psycopg2 

root = Tk()
root.title('Vypocet BMI')
root.geometry('300x300')
root.resizable(False, False)

# Functions ===================================================================
def calculate_bmi(weight, height):
    text_result = ''
    bmi = round(float(weight) / float(height) ** 2, 2)
    if bmi < 18.5:
        text_result = 'podvaha'
    elif bmi < 24.9:
        text_result = 'normalni'
    elif bmi < 29.2:
        text_result = 'nadvaha'
    elif bmi < 34.9:
        text_result = 'obezita'
    elif bmi >= 34.9:
        text_result = 'extremni obezita'
    
    label_user_result_1['text'] = bmi
    label_user_result_2['text'] = text_result

    insert_data(bmi, text_result)

def check_dot(number):
    number_string = str(number)
    if ',' in number_string:
        return number_string.replace(',', '.')
    return number_string

def insert_data(bmi_name, bmi_text):
    connection = psycopg2.connect(
        dbname = 'health',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    cursor = connection.cursor()
    query = '''INSERT INTO bmi(bmi_number, bmi_text) VALUES (%s, %s)'''
    cursor.execute(query, (bmi_name, bmi_text))
    connection.commit()
    connection.close()

def count_all_data():
    connection = psycopg2.connect(
        dbname = 'health',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    cursor = connection.cursor()
    query = '''SELECT COUNT(bmi_id) FROM bmi'''
    cursor.execute(query)
    count = cursor.fetchone()
    connection.close()
    return count[0]

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
button = Button(root, text = 'Vypocitat', command = lambda:calculate_bmi(check_dot(entry_weight.get()), check_dot(entry_height.get())))
button.grid(row = 3, column = 1)

# result section ==============================================================
label_result_1 = Label(root, text = 'Ciselny vysledek:')
label_result_1.grid(row = 4, column = 0)

label_user_result_1 = Label(root)
label_user_result_1.grid(row = 4, column = 1)

label_result_2 = Label(root, text = 'Textovy vysledek:')
label_result_2.grid(row = 5, column = 0)

label_user_result_2 = Label(root)
label_user_result_2.grid(row = 5, column = 1)

label_count_text = Label(root, text = 'Pocet uzivatelu:')
label_count_text.grid(row = 6, column = 0)

label_count_number = Label(root, text = count_all_data())
label_count_number.grid(row = 6, column = 1)

root.mainloop()