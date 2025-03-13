import psycopg2 # type: ignore

#configuracion de la base 
DB_CONFIG = {
    "dbname": "etl_db",
    "user": "user",
    "password": "password",
    "host": "postgres",
    "port": "5432"
}
#carga de la data desde la base 
def load_data(data):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            for movie in data:
                cursor.execute(
                    "INSERT INTO etl_data (id, nombre, categoria, decada, puntuacion) VALUES (%s, %s, %s, %s, %s)",
                    (movie["id"], movie["nombre"], movie["categoria"], movie["decada"], movie["puntuacion"])
                )
        conn.commit()
