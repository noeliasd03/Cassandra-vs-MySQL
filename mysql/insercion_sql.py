import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configurar la conexión a la base de datos
host = 'localhost'  
database = 'tu_base_de_datos'
user = 'tu_usuario'
password = 'tu_contraseña'

# Leer el archivo CSV en un DataFrame
csv_file_path = '../datos.csv'  # Cambia a la ruta de tu archivo CSV
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
        insert_query = '''
        INSERT INTO tu_tabla (id, name, age, city) VALUES (%s, %s, %s, %s)
        '''
        for _, row in df.iterrows():
            cursor.execute(insert_query, (int(row['id']), row['name'], int(row['age']), row['city']))
        connection.commit()
        print("Datos insertados con éxito en MySQL")

except Error as e:
    print("Error al conectar a MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a MySQL cerrada")
