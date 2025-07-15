# test_db_connection.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Cargamos el archivo .env
load_dotenv()
print("--- Intentando conectar a la base de datos ---")

db_url = os.environ.get("DATABASE_URL")

if not db_url:
    print("ERROR: La variable de entorno DATABASE_URL no fue encontrada.")
else:
    print(f"URL encontrada: {db_url}")
    try:
        # Intentamos crear el motor de SQLAlchemy
        engine = create_engine(db_url)

        # Intentamos establecer una conexión real
        with engine.connect() as connection:
            print("¡Conexión exitosa!")

            # Ejecutamos una consulta simple para verificar
            result = connection.execute(text("SELECT 1"))
            for row in result:
                print(f"Resultado de la consulta de prueba: {row}")

    except Exception as e:
        print("\n--- Ocurrió un error al conectar ---")
        print(f"Tipo de error: {type(e).__name__}")
        print(f"Error: {e}")
        print("-------------------------------------")
        print("\nPor favor, verifica lo siguiente:")
        print("1. ¿El servidor de PostgreSQL está corriendo en el puerto 5432?")
        print("2. ¿La base de datos 'producthunt_db' existe en tu pgAdmin4?")
        print("3. ¿El usuario 'postgres' tiene permisos para acceder a 'producthunt_db'?")