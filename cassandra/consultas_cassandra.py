import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import os 
current_dir = os.getcwd()
keyspace = 'store'
table = 'users'
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

session.execute(f'''
CREATE KEYSPACE IF NOT EXISTS {keyspace}
WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
''')

session.set_keyspace(keyspace)

query = f"SELECT age FROM {table}"
rows = session.execute(query)

df = pd.DataFrame(rows, columns=['age'])

media_age = df['age'].mean()
print(f"La media de edad es: {media_age}")

cluster.shutdown()
