from utils.tikidb_config  import read_db_config
import psycopg2
from psycopg2 import Error
from database.connect import connect_db

table_exexute = 'CREATE TABLE IF NOT EXISTS products\
                        (\
                            id VARCHAR(255),\
                            brand VARCHAR(255),\
                            category TEXT,\
                            price VARCHAR(255),\
                            discount VARCHAR(255),\
                            title VARCHAR(255),\
                            total_sales VARCHAR(255),\
                            rating VARCHAR(255),\
                            image_link TEXT,\
                            product_link TEXT,\
                            from_page_link TEXT\
                        )'

def db_init():
    conn = None
    try: 
        conn = connect_db()
        if conn:
            print('Connected to Postgresql database')
            cursor = conn.cursor()
            # Execute the table creation query
            cursor.execute(table_exexute)
            conn.commit() # commit the transaction
            print('table ccreated seccessfully')
    
    except Error as e:
            print(e)
    finally:
        if conn is not None:
             cursor.close()
             conn.close()
             print("Connection closed")

if __name__ =='__main__':
     db_init()