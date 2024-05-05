import psycopg2

def create():
    connection = psycopg2.connect(
        dbname = 'student',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE teacher(
            ID SERIAL,
            NAME TEXT,
            AGE INT,
            ADDRESS TEXT
        )    
    ''')

    connection.commit()
    connection.close()

def insert_data():
    connection = psycopg2.connect(
        dbname = 'student',
        user = 'name',
        password = 'pass',
        host = '127.0.0.1',
        port = '5432'
    )

    teacher_name = input('Jmeno ucitele: ')
    teacher_age = input('Vek ucitele: ')
    teacher_address = input('Adresa ucitele: ')

    cursor = connection.cursor()
    query = '''INSERT INTO teacher(name, age, address) VALUES (%s, %s, %s)'''
    cursor.execute(query, (teacher_name, teacher_age, teacher_address))
    connection.commit()
    connection.close()

insert_data()