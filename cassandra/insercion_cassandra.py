import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

csv_file_path = '../datos.csv'  
keyspace = 'store' ## PENDIENTE
table = 'users'

df = pd.read_csv(csv_file_path)

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
session.execute(f'''
CREATE TABLE IF NOT EXISTS {table} (
    id int PRIMARY KEY,
    name text,
    age int,
    city text
)
''')

insert_statement = SimpleStatement(f'''
INSERT INTO {table} (id, name, age, city) VALUES (%s, %s, %s, %s)
''')

for _, row in df.iterrows():
    session.execute(insert_statement, (int(row['id']), row['name'], int(row['age']), row['city']))

cluster.shutdown()
