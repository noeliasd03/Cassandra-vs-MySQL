# Cassandra-vs-MySQL
Diferencias de rendimiento entre Cassandra y MySQL.


## Instrucciones:

**1º Crear enviroment**   

`conda env create --file config_environment.yml`

---

**2º Entra en el enviroment**   

`conda activate basesdatos`

---

**3º Levantar servidores Cassandra y MySQL**

`docker compose -f docker-compose-cassandra.yml up -d`   
`docker compose -f docker-compose-mysql.yml up -d`

Para comprobar que los servidores están corriendo:  

`docker ps`

Para conectarse a los servidores:

`docker exec -it cassandra-server cqlsh`     
`docker exec -it mysql-server mysql -u root -p` (ingresar contraseña: changeme)

---

**4º Carga de scripts**

Para cargar los datos en el servidor **Cassandra**:  
Ejecutas el script    
`python cassandra/insercion_cassandra.py`  
Ahora al entrar en el servidor puedes observar los datos  
`docker exec -it cassandra-server cqlsh`       
`use store;`  
`select * from users;`

Para cargar los datos en el servidor **MySQL**:  
Ejecutas el script    
`python mysql/insercion_mysql.py`  
Ahora al entrar en el servidor puedes observar los datos    
`docker exec -it mysql-server mysql -u root -p` (ingresar contraseña: changeme)         
`use store;`        
`select * from users;`

---

**5º Consultas**

Para consultar la media de edad en Cassandra ejecutar:

`python cassandra/consultas_cassandra.py`

Para consultar la media de edad en MySQL ejecutar:

`python mysql/consultas_sql.py`

Para poder hacer la comparativa de los tiempos de ejecución abrir 'comparativa.ipynb' y ejecutarlo. 

