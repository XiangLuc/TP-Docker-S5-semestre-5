import psycopg

def get_db_password():
    with open('/run/secrets/db_password', 'r') as file:
        password = file.read().strip()
    return password

db_password = get_db_password()

conn = psycopg.connect(f'dbname=tp user=luc host=db password={db_password}')

def close_connection():
    if conn:
        conn.close()