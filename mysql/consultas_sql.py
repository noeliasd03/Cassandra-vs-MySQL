import pandas as pd
import mysql.connector
from mysql.connector import Error
import os
# Configurar la conexión a la base de datos
host = '127.0.0.1'  
database = 'store'
user = 'root'
password = 'changeme'

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
        avg_age_query = '''
            SELECT AVG(age) AS promedio_age FROM users
        '''
        cursor.execute(avg_age_query)
        result = cursor.fetchone()
        print(f"La media de edad (age) es: {result[0]}")
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


except Error as e:
    print("Error al conectar a MySQL", e)

