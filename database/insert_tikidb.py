from utils.tikidb_config import read_db_config
import psycopg2
import sys
from database.connect import connect_db

def insert_data(data):
    conn= connect_db()
    if conn is None:
        return

    query = 'INSERT INTO products(id, brand, category, price, discount, title, total_sales, rating, image_link, product_link, from_page_link)'\
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    args = [str(item) for item in data]

    try: 
        
        with conn.cursor() as cursor:
            cursor.execute(query, args)
        conn.commit()
        print("Data insert successfully ")
    except Exception as error:
        print('error')
        sys.exit(1)
    finally:
        conn.close()
        cursor.close()