#libreria con el driver para conectarse a una base de datos MySQL
import mysql.connector

#funcion que conecta con la base de datos
miBase = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

#print(miBase) imprime el nombre de la base de datos
