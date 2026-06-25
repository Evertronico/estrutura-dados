# Conexão com o MySQL
import mysql.connector

# Função de conexão com o bd
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='secretaria_saude'
    )
