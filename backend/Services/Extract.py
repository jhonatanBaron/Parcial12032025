from neo4j import GraphDatabase

URI = "bolt://neo4j:7687"
AUTH = ("neo4j", "test")
#funcion para extraer los datos de la base de datos
def extract_data():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        query = "MATCH (p:Movie) RETURN p.id, p.nombre, p.calificacion, p.año_lanzamiento, p.genero"
        with driver.session() as session:
            result = session.run(query)
            return [{"id": record["p.id"], "nombre": record["p.nombre"], 
                     "calificacion": record["p.calificacion"], 
                     "año_lanzamiento": record["p.año_lanzamiento"], 
                     "genero": record["p.genero"]} for record in result]
