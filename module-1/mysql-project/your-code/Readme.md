Selecciono base de datos HOCKEY que contiene diversas tablas de jugadores de hockey y entrenadores. 


Genero el diagrama EDR

![/home/cristina/Ironhack/PRACTICA_MYSQL/PRACTICASQL2/EER HCKEY.png]

**PRIMERA QUERY:**
De dos tablas diferentes, una con jugadores y  otra de jugadores premiados, extraigo el total de jugadores premiados agrupados por nombre en orden ascendente, utilizo la instrucción Inner join

    SELECT Master1.nameGiven
    FROM Master1
    INNER JOIN AwardsPlayers
    ON Master1.playerID = AwardsPlayers.playerID
    GROUP BY Master1.nameGiven
    ORDER BY Master1.nameGiven ASC;

**SEGUNDA QUERY:**
La información que proporciona la base de daros es bastante limitada ya que no se entienden las cabeceras de las columnas ni hay relaciones por ejemplo entre jugadores y equipos o jugadores y entrenadores. Introduzo una consulta que me devuelve los id de los jugadores, su  nombre, País de nacimiento y como restricciones establezco que hayan nacido en Finlandia y su altura sea de 72, ordenada por Id de jugador en orden ascendente
    SELECT Master1.playerID, Master1.nameGiven, Master1.birthCountry
    FROM Master1
    WHERE Master1.birthCountry = "Finland" AND Master1.height = 72
    ORDER BY Master1.playerID ASC;

**TERCERA QUERY:**
Decido contar el número de jugadores que hay por cada país de origen y estatura media por país de origen, ordenada por el número de jugadores por país de menor a mayor

    SELECT DISTINCT Master1.birthCountry, COUNT(*) as Players, AVG(Master1.height) as AVGHeight
    FROM Master1
    GROUP BY Master1.birthCountry
    ORDER BY Players ASC;

**CUARTA QUERY:**
Seguimos con la limitaciones de los datos, decido crear una nueva tabla que contenga número de goles por partido y  por jugador, (presuponiendo que esos podrían ser los datos que arroja la tabla que escojo). La nueva tabla la nombro la nombro golespartido

    CREATE TABLE golespartido
    SELECT DISTINCT GoaliesShootout.playerID, SUM(GoaliesShootout.SA) AS Goles, SUM(GoaliesShootout.GA) AS Partidos
    FROM GoaliesShootout
    GROUP BY playerID
    ORDER BY playerID

Refresco el panel de Schemas y aparece la tabala nueva que hemos creado

**QUINTA QUERY:** 
Utilizando la tabala nueva y haciendo un inner join con la principal que contine casi todala información, genero una subquery que me de el número de jugadores por país, su estaura media, el total de goles y de partidos. A esta subquery le lanzo una consulta de la que obtengo el número de goles medios por país, así como la estatura media de los jugadores de ese país, con el fin de establecer una relación que me diga si en función de la estatura media de un país se marcan más goles o no

    SELECT Country, Total_goles/Total_partidos as Goles_medios, AVGHeight
    FROM (
        SELECT DISTINCT Master1.birthCountry as Country, COUNT(*) as Players, AVG(Master1.height) as AVGHeight, SUM(golespartido.Goles) as Total_goles, SUM(golespartido.Partidos) as Total_partidos
        FROM Master1
        INNER JOIN golespartido
        ON Master1.playerID = golespartido.playerID
        GROUP BY Master1.birthCountry
        ORDER BY Master1.birthCountry) summary;
