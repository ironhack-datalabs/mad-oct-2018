 -- RELACIÓN JUGADORES PREMIADOS AGRUPADOS Y ORDENADOS POR NOMBRE 
 
SELECT Master1.nameGiven
FROM Master1
INNER JOIN AwardsPlayers
ON Master1.playerID = AwardsPlayers.playerID
GROUP BY Master1.nameGiven
ORDER BY Master1.nameGiven ASC;

 -- RELACION  JUGADORES CUYO PAÍS DE ORIGEN ES FINLANDIA Y TIENEN ESTATURA 72 ORDENADOS POR ID DE JUGADOR
SELECT Master1.playerID, Master1.nameGiven, Master1.birthCountry
FROM Master1
WHERE Master1.birthCountry = "Finland" AND Master1.height = 72
ORDER BY Master1.playerID ASC;

 -- NÚMERO DE JUGADORES QUE HAY POR PAÍS DE ORIGEN Y MEDIA DE SU ESTATURA
SELECT DISTINCT Master1.birthCountry, COUNT(*) as Players, AVG(Master1.height) as AVGHeight
FROM Master1
GROUP BY Master1.birthCountry
ORDER BY Players ASC;


 -- CREACIÓN DE TABLA NUEVA QUE ME INDICA EL NÚMERO DE GOLES Y EL NÚMERO DE PARTIDOS POR ID DE JUGADOR
CREATE TABLE golespartido
SELECT DISTINCT GoaliesShootout.playerID, SUM(GoaliesShootout.SA) AS Goles, SUM(GoaliesShootout.GA) AS Partidos
FROM GoaliesShootout
GROUP BY playerID
ORDER BY playerID;


 -- UNIENDO LA TABLA ANTERIOR Y LA PRINCIPAL MEDIANTE UN INNER JOIN CONSIGO LA RELACIÓN DE GOLES MEDIOS POR PAÍS DE ORIGEN ASÍ COMO SU ESTATURA MEDIA

SELECT Country, Total_goles/Total_partidos as Goles_medios, AVGHeight
FROM (
	SELECT DISTINCT Master1.birthCountry as Country, COUNT(*) as Players, AVG(Master1.height) as AVGHeight, SUM(golespartido.Goles) as Total_goles, SUM(golespartido.Partidos) as Total_partidos
	FROM Master1
	INNER JOIN golespartido
	ON Master1.playerID = golespartido.playerID
	GROUP BY Master1.birthCountry
	ORDER BY Master1.birthCountry) summary;



