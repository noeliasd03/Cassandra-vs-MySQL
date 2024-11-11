import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import os 
current_dir = os.getcwd()
csv_file_path = os.path.abspath(os.path.join(current_dir, 'datos.csv'))
keyspace = 'store'
table = 'users'
df = pd.read_csv(csv_file_path)
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

session.execute(f'''
CREATE KEYSPACE IF NOT EXISTS {keyspace}
WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
''')

session.set_keyspace(keyspace)

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

print("Datos insertados con éxito en Cassandra")

cluster.shutdown()
