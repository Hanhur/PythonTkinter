import bcrypt, psycopg2
from tkinter import *

def password_to_hash(plain_password):
    try:
        password_bytes = plain_password.encode('utf-8')
        hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hash
    except Exception as error:
        print(f'Error pri hashovani hesla: {error}')
        return None

def insert_bank_user(email, password):
    try:
        connection = psycopg2.connect(
            dbname = 'bank',
            user = 'name',
            password = 'pass',
            host = '127.0.0.1',
            port = '5432'
        )

        cursor = connection.cursor()
        query = '''INSERT INTO bank_user(email, password) VALUES(%s, %s)'''
        hash = password_to_hash(password)
        cursor.execute(query, (email, hash))
        connection.commit()
        connection.close()
    except psycopg2.DatabaseError as error:
        print(f'Error database: {error}')
    except Exception as error:
        print(f'Obecna chyba: {error}')

def get_hash_from_database(email):
    try:
        connection = psycopg2.connect(
            dbname = 'bank',
            user = 'name',
            password = 'pass',
            host = '127.0.0.1',
            port = '5432'
        )

        cursor = connection.cursor()
        query = '''SELECT password FROM bank_user WHERE email=(%s)'''
        cursor.execute(query , (email,))
        user_hash_password = cursor.fetchone()
        connection.close()

        if user_hash_password:
            return bytes.fromhex(user_hash_password[0][2:])
        else:
            return b''
    except psycopg2.DatabaseError as error:
        print(f'Error database: {error}')
        return b''
    except Exception as error:
        print(f'Obecna chyba: {error}')
        return b''
    
def login_authentication(password, email):
    try:
        hash = get_hash_from_database(email)
        password_bytes = bytes(password, encoding = 'utf-8')
        if hash == b'':
            result_label['text'] = 'Neplatne'
        else:
            if bcrypt.checkpw(password_bytes, hash):
                result_label['text'] = 'Uspesne prihlaseni'
            else:
                result_label['text'] = 'Neplatne'
    except Exception as error:
        result_label['text'] = 'Doslo k chybe pri overovani'
        print(f'Chyba pri overovani: {error}')


root = Tk()
root.title('Regisnrace a priglaseni')
root.geometry('300x300')
root.resizable(False, False)

# Registration section =======================================================
regisration_label = Label(text = 'Registrace')
regisration_label.grid(row = 0, column = 1)

email_label = Label(text = 'Email: ')
email_label.grid(row = 1, column = 0)

email_entry = Entry()
email_entry.grid(row = 1, column = 1)

password_label = Label(text = 'Heslo: ')
password_label.grid(row = 2, column = 0)

password_entry = Entry(show = '*')
password_entry.grid(row = 2, column = 1)

registration_button = Button(text = 'Zaregistrovat', command = lambda:insert_bank_user(email_entry.get(), password_entry.get()))
registration_button.grid(row = 3, column = 1)

# Login section
login_label = Label(text = 'Prihlaseni')
login_label.grid(row = 4, column = 1)

email_login_label = Label(text = 'Email: ')
email_login_label.grid(row = 5, column = 0)

email_login_entry = Entry()
email_login_entry.grid(row = 5, column = 1)

password_login_label = Label(text = 'Heslo: ')
password_login_label.grid(row = 6, column = 0)

password_login_entry = Entry(show = '*')
password_login_entry.grid(row = 6, column = 1)

login_button = Button(text = 'Prihlasit se', command = lambda:login_authentication(password_login_entry.get(), email_login_entry.get()))
login_button.grid(row = 7, column = 1)

# Result section
result_label = Label()
result_label.grid(row = 8, column = 1)

root.mainloop()