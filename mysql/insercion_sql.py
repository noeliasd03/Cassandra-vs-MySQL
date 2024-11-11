import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

host = '127.0.0.1'  
database = 'store'
user = 'root'
password = 'changeme'

# Leer el archivo CSV en un DataFrame
current_dir = os.getcwd()
csv_file_path = os.path.abspath(os.path.join(current_dir, 'datos.csv'))
df = pd.read_csv(csv_file_path)


try:
    # Conectarse a la base de datos
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )



    if connection.is_connected():
        cursor = connection.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                city VARCHAR(100)
            )
            '''
        cursor.execute(create_table_query)


        insert_query = '''
        INSERT INTO users (id, name, age, city) VALUES (%s, %s, %s, %s)
        '''
        for _, row in df.iterrows():
            cursor.execute(insert_query, (int(row['id']), row['name'], int(row['age']), row['city']))
        connection.commit()
        print("Datos insertados con éxito en MySQL")
        
        if connection.is_connected():
            cursor.close()
            connection.close()


except Error as e:
    print("Error al conectar a MySQL", e)

