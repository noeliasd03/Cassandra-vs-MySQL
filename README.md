# Cassandra-vs-MySQL
Diferencias de rendimiento entre Cassandra y MySQL.
conda create --name 'name_environment' python=3.7

# Instrucciones:

1º crear enviroment   

`conda env create --file config_enviroment.yml`

2º entra en el enviroment   

`conda activate basesdatos`

3º levantar servidores Cassandra y MySQL

`docker-compose -f docker-compose-cassandra.yml up -d`
`docker-compose -f docker-compose-mysql.yml up -d`

Para conectarse a los servidores:

`docker exec -it cassandra-server cqlsh` 

