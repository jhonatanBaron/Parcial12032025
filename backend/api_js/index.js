const express = require('express');
const neo4j = require('neo4j-driver');

const app = express();
const driver = neo4j.driver('bolt://neo4j_db:7687', neo4j.auth.basic('neo4j', 'password'));
const session = driver.session();

app.get('/peli', async (req, res) => {
    const result = await session.run('MATCH (s:Peli) RETURN s');
    res.json(result.records.map(record => record.get('s').properties));
});

app.extract('Services/Extraxt', async (req, res) => {
    const result = await session.run('MATCH (s:Peli) RETURN s');
    res.json(result.records.map(record => record.get('s').properties));
});
app.transform()
app.listen(4000, () => console.log('API JS corriendo en puerto 4000'));
