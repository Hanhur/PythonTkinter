import bcrypt, psycopg2

def password_to_hash(plain_password):
    password_bytes = plain_password.encode('utf-8')
    hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hash


def insert_bank_user(email, password):
    connection = psycopg2.connect(
        dbname = 'bank',
        user = 'mame',
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

def get_hash_from_database(email):
    connection = psycopg2.connect(
        dbname = 'bank',
        user = 'mame',
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
    
def login_authentication(password, email):
    hash = get_hash_from_database(email)
    password_bytes = bytes(password, encoding = 'utf-8')
    if hash == b'':
        print('Neplatne')
    else:
        if bcrypt.checkpw(password_bytes, hash):
            print('Uspesne prihlaseni')
        else:
            print('Neplatne')


















# Registrace
# password = b'admin'
# hash = bcrypt.hashpw(password, bcrypt.gensalt())

# # Prihlaseni
# user_password = input('Napiste sve heslo: ')
# user_password = bytes(user_password, encoding = 'utf-8')

# if bcrypt.checkpw(user_password, hash):
#     print('Uspesne prihlaseni')
# else:
#     print('Spatne zadane heslo')