from neo4j import GraphDatabase

NEO4J_URI = "bolt://neo4j_db:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def get_all_Peli():
    query = "MATCH (s:Peli) RETURN s"
    with driver.session() as session:
        result = session.run(query)
        return [record["s"] for record in result]

def get_Peli(Peli_id):
    query = "MATCH (s:Peli {id: $id}) RETURN s"
    with driver.session() as session:
        result = session.run(query, id=Peli_id)
        return result.single()["s"]

def create_Peli(data):
    query = "CREATE (s:Peli {id: $id, nombre: $nombre, calificacion: $calificacion, anio: $anio,lanzamiento: $lanzamiento,genero: $genero}) RETURN s"
    with driver.session() as session:
        result = session.run(query, **data)
        return result.single()["s"]
