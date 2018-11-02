# Guided Project: API and Web Data Scraping

## API | Rick and Morty API

### Introducción
Mi ejercicio trabaja sobre una API de la famosa serie de animación que se encuentra en la siguiente URL. 
```
https://rickandmortyapi.com/
```
Para mayor claridad de código las funciones auxiliares se encuentran en el fichero **funciones.py** localizado en la misma carpeta que todo el proyecto. La carpeta **output** contendrá todos los archivos CSV de salida. 

El jupyter notebook pedirá los números de los episodios que queremos analizar y devolverá la información en forma de DataFrame y los guardará en un CSV en la carpeta correspondiente. el nombre del CSV contendrá los números de los episodios consultados. 
Ejemplo de petición de datos sobre el episodio 1
```
episodes": "https://rickandmortyapi.com/api/episode/1
```
Obtenemos: 
```
id	1
name	"Pilot"
air_date	"December 2, 2013"
episode	"S01E01"
characters	
0	"https://rickandmortyapi.com/api/character/1"
1	"https://rickandmortyapi.com/api/character/2"
2	"https://rickandmortyapi.com/api/character/35"
3	"https://rickandmortyapi.com/api/character/38"
4	"https://rickandmortyapi.com/api/character/62"
5	"https://rickandmortyapi.com/api/character/92"
6	"https://rickandmortyapi.com/api/character/127"
7	"https://rickandmortyapi.com/api/character/144"
8	"https://rickandmortyapi.com/api/character/158"
9	"https://rickandmortyapi.com/api/character/175"
10	"https://rickandmortyapi.com/api/character/179"
11	"https://rickandmortyapi.com/api/character/181"
12	"https://rickandmortyapi.com/api/character/239"
13	"https://rickandmortyapi.com/api/character/249"
14	"https://rickandmortyapi.com/api/character/271"
15	"https://rickandmortyapi.com/api/character/338"
16	"https://rickandmortyapi.com/api/character/394"
17	"https://rickandmortyapi.com/api/character/395"
18	"https://rickandmortyapi.com/api/character/435"
url	"https://rickandmortyapi.com/api/episode/1"
created	"2017-11-10T12:56:33.798Z"
```
Ejemplo de petición de datos sobre el personaje dado: 
```
https://rickandmortyapi.com/api/character/92
```
### Primera iteración
Se pregunta a la API los números de episodios existentes y este dato acota los valores permitidios a la hora de requerir los episodios correspondientes. Para asegurarnos de ello he realizado programación defensiva en la función correspondiente que pide números enteros uno cada vez y sólo valen los correspondientes a los episodios existentes. 

De cada episodio obtenemos de la api los personajes que aparecen y por cada personaje obtenemos también de la api sus nombres. Creamos un DataFrame con el número de apariciones y su porcentaje en el total de los episodios cuestionados mediante una simple operación sobre la columna. 

El DataFrame se guarda en un archivo CSV en la carpeta **output** con un nombre personalizado. Si por ejemplo hemos cuestionado por los episodios 6 y 7, el nombre será: 
```
6-7output.csv
```
### Segunda iteración
La función que toma los números de los episodios acepta un string de números separados por comas. Por ejemplo sugiero usar: 6,7 puesto que los resultados en el dataframe sorprenderán. 

Reutilizo la función **get_terms()** del proyecto previo **BoW (bag of words)** pero modificado permitiendo incluir {N, 0} en vez de {1, 0} indicar con N el número de apariciones, ya que en esta serie de ciencia ficción los personajes se encuentran con realidades alternativas suyas. La he mejorado para que use List Comprehensions. 

El Dataframe de **BoW (bag of words)** se concatena con el resultado de la iteración 1. para obtener una tabla donde además de los porcentajes de apariciones, se observe en cada columna correspondiente a cada episodio, si ha aparecido o no, así como el número de versiones de realidades alternativas. 

### Mejoras futuras
1. Permitir que la toma de episodios permita un formato tal que así: 4, 5, 7-11, 12
2. Reducir el número de peticiones a la API puesto que si un personaje ya ha sido consultado para obtener su nombre, deberiamos almacenar la consulta para no tener que realizarla repetidas veces. 
3. Preguntar el nombre del fichero de salida para guardar los datos. 
4. La columna del capítulo debería tener el número (o el nombre) de dicho capítulo y no ser: 0, 1, 2, 3 etc que corresponden al orden de petición. 

## Scraping | Wikipedia

### Introducción
En este ejercicio vamos a recopilar los datos personales de un personaje que tenga página en wikipedia. Los vamos a obtener de la tabla que aparece arriba a la derecha de cada página que consultemos. 

### Primera iteración
Observamos la web **https://es.wikipedia.org/wiki/Stephen_King** como primer intento.
#### Problema
la estructura de dicha tabla es por ejemplo: 
```
<table>
    <tbody>
        <tr>
            <th>
            <th>
            <td>
            <th>
            <td>
            <tr>
```   
Donde cada dato a capturar tiene su nombre dentro de ```<th>``` y su valor en ```<td>```. Pero los ```<th>``` que no preceden a un ```<td>``` son una fila que no aporta información. Así que habrá que hacer un filtrado más complejo. 
```
url = 'https://es.wikipedia.org/wiki/Stephen_King'
html_king = requests.get(url).content
soup_king = BeautifulSoup(html_king, "lxml")

datos = [(e.find_previous_sibling('th').text, e.text.strip()) for e in soup_king.select('table tbody tr th + td')]
```
Que nos devuelve una lista de tuplas (nombre_variable, valor_variable). Dicha tupla la podemos poner en un DataFrame de la librería pandas y mostrarlo por pantalla. 
### Segunda iteración
Implementamos en una función que se pueda pedir por consola el nombre del famoso que queremos observar. Ponemos algunas mejoras para que traduzca los espacios y minúsculas de **'stephen king'** a lo que la web de wikipedia necesita **'Stephen_King'**.
Asimismo reutilizaremos el código de salvar dataframe como csv en un archivo utilizado en el ejercicio de **API** aprovechando que pusimos nombre y path como atributos opcionales en la cabecera. Lo salvamos con el nombre del personaje en cuestión
```
save_df(df_p, fname=personaje+'.csv')

```




