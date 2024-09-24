from utils.tikidb_config import read_db_config
import psycopg2
from psycopg2 import OperationalError

def connect_db():
    conn = None
    try:
        db_config = read_db_config(section='postgresql')
        print('Connecting to Postgresql database ...')
        conn= psycopg2.connect(**db_config)
        print('Connection established')
    except OperationalError as e:
        print(f'Error: {e}')
    finally:
        if conn is not None:
            conn.close()
            print("Connection close")
if __name__=='__main__':
    connect_db





