import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def get_db_connection():
    """Crea y retorna una conexión a la base de datos PostgreSQL."""
    try:
        conexion = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None

# Prueba rápida de conexión
if __name__ == '__main__':
    conn = get_db_connection()
    if conn:
        print("¡Conexión exitosa a la base de datos Cueva de Petra!")
        conn.close()