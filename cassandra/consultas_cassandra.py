import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import os 
current_dir = os.getcwd()
keyspace = 'store' ## PENDIENTE
table = 'users'
cluster = Cluster(['127.0.0.1'])  # PENDIENTE
session = cluster.connect()
# Crear el keyspace si no existe
session.execute(f'''
CREATE KEYSPACE IF NOT EXISTS {keyspace}
WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
''')
# Conectarse al keyspace
session.set_keyspace(keyspace)
# Crear la tabla si no existe
query = f"SELECT age FROM {table}"
rows = session.execute(query)

# Cargar los datos en un DataFrame de Pandas
df = pd.DataFrame(rows, columns=['age'])

# Calcular la media de la columna 'age'
media_age = df['age'].mean()
print(f"La media de edad es: {media_age}")

cluster.shutdown()