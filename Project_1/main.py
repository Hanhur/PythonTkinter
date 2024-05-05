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

    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO teacher(name, age, address) 
        VALUES ('McGonagallove', 50, 'Bradavice')  
    ''')

    connection.commit()
    connection.close()
