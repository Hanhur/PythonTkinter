import psycopg2
from psycopg2 import pool

# Init pool
db_pool = pool.SimpleConnectionPool(1, 10, 
    dbname = 'student',
    user = 'name',
    password = 'pass',
    host = '127.0.0.1',
    port = '5432'
)

def create_table():
    with db_pool.getconn() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE teacher(
                    ID SERIAL,
                    NAME TEXT,
                    AGE INT,
                    ADDRESS TEXT
                )    
            ''')
            connection.commit()
        db_pool.putconn(connection)


def insert_data(teacher_name, teacher_age, teacher_address):
    with db_pool.getconn() as connection:
        with connection.cursor() as cursor:
            query = '''INSERT INTO teacher(name, age, address) VALUES (%s, %s, %s)'''
            cursor.execute(query, (teacher_name, teacher_age, teacher_address))
            connection.commit()
        db_pool.putconn(connection)

insert_data('Brumbal', 45, 'Bradavice')