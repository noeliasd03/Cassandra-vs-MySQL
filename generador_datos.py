import os
import pandas as pd
from faker import Faker
import random

# Obtener el directorio de trabajo actual
current_dir = os.getcwd()

# Definir una ruta dentro del directorio actual para guardar el archivo
csv_file_path = os.path.join(current_dir, 'datos.csv')  # Esto guarda en el directorio actual

# Generar datos de ejemplo
fake = Faker()
num_records = 10
data = {
    'id': list(range(1, num_records + 1)),
    'name': [fake.name() for _ in range(num_records)],
    'age': [random.randint(18, 80) for _ in range(num_records)],
    'city': [fake.city() for _ in range(num_records)]
}

# Crear y guardar el DataFrame
df = pd.DataFrame(data)
df.to_csv(csv_file_path, index=False)