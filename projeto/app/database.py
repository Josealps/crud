import psycopg2
import alembic

def conecta():
    try:
        connect = psycopg2.connect(
            host="postgres_joses",
            database="crud",
            user="postgres",
            password="postgres"
        )
        print("Conectado com sucesso!")
        return connect
    except psycopg2.Error as e:
        print(f"Erro ao conectar: {e}")
        return None

def encerrar_session(connect):
    if connect:
        connect.close()
        print("Conexão encerrada com sucesso!")

conexao = conecta()
if conexao:
    encerrar_session(conexao)