# Web Project

## Obtener datos de una API usando Python
### 1. Elegir base de datos. 
Después de investigar varias API procedentes de los dos enlaces proporcionados en la práctica. Me he decicio por "Makeup API" (http://makeup-api.herokuapp.com/). Una API que no requiere autentificación y tiene diferentes datos de 930 productos de belleza de una web. <br>

### 2. Hipótesis (finalidad)
Supongamos que trabajamos para una marca de cosméticos y quiere lanzar al mercado diferentes tipos de productos. <br>

El perfil de consumidor de la web es nuestro principal target: Mujer, entre 30-40 años, urbanita, poder adquisitivo medio, interés por las últimas tendencias en moda, preocupada por el aspecto físico y asidua a compras por internet. <br>

Queremos analizar, en esta web, por tipos de productos, marcas y precio de los mismos.  <br>


### 3. Exportar datos. 
Exportamos los datos a través del comando request, al ser un archivo JSON, nos podemos permitir normalizarlo a través de "json_normalize". Nos devuelve una tabla que aún no sabemos que tipo de datos. <br>
Para ello aplicamos .info y vemos que nuestro dataset es de clase Dataframe, con 931 entradas (filas) una por cada producto, y 19 columnas con información sobre: <br> 

### 4. Data Cleaning 

Eliminamos columnas con información que no es necesaria: api_featured_image, image_link, product_api_url. <br>

He intentado normalizar la columna de "product_colors"  de varias maneras a través de json.normalize. Es el punto donde me he atascado. No he podido, como es una información que a la hora de desarrollar un nuevo producto de cosmética nos puede ser de utilidad, nos quedamos con la columna aunque sea sin normalizar. <br>

Ordenamos nuestras columnas. <br>

### 5. Extraemos listas
Extraemos los valores únicos de la columna brand y la columna product_type. Para incluir las listas en nuestra función. 

### 6. Definimos nuestra función
Nuestra función requiere dos inputs: marca y producto que requiera analizar. Primero imprimimos ambas listas procedentes de la columnas para que el usuario pueda ver las marcas y los tipos de productos existentes. <br>
Una vez haya elegido ambos inputs la función le devuelve un dataframe con solo los atributos seleccionados procedente de nuestro dataframe extraido de nuestra api. 



## Web Scraping con python

### 1. Primer scraping 
Queremos saber los 50 primeros grupos de tecnología en Madrid en la página de meetup Meetup. <br>
https://www.meetup.com/es-ES/find/tech/ <br>

* Para ello utilizamos request y beautiful soup. Creamos una condición sobre cada item de la primera búsqueda (que es la búsqueda sobre todos los eventos en general). De cada grupo, extraemos la información del nombre del grupo y del número de miembros que están apuntados. <br>
* Después creamos un dataframe uniendo la lista de títulos y la de miembros. <br>
* Dividimos la columna Members para tener por separado en dos columnas, el número de miembros del grupo y el nombre de esos miembros. <br>
* Imprimimos nuestros resultados en un dataframe <br>

### 2. Segundo scraping
Ahora queremos conocer los próximos eventos en tecnología, el grupo que lo organiza y la cantidad de miembros que van a asistir. <br>
* Exportamos la información de la página https://www.meetup.com/es-ES/find/events/tech/?allMeetups=false&radius=31&userFreeform=Madrid%2C+Espa%C3%B1a&mcId=z1010808&mcName=Madrid%2C+ES&eventFilter=all' con beutiful soup <br>
* Hemos tenido problemas para encontrar exactamente las etiquetas de cada elemento de la web. Hemos utilizado find_all y select en diferentes ocasiones para extraer exactamente la información concreta. Esto nos ha llevado bastante tiempo, la página tiene multitud de elementos. <br>
* Una vez tenemos toda la información, el nombre del grupo, el nombre del evento y los asistentes al evento, hemos dividido (como anteriormente), la columna "Audience" para tener en dos columnas: el número de asistentes y el el nombre de esos miembros del grupo. <br>
* Nos hemos dado cuenta de que el "Event_name" en la posición 9 en la página web tiene una clase diferente al resto, por lo que nuestro web scraping a partir del elemento 9 nos da como resultado el "Group_name" de la posición 9 con el "Event_name" de la posición 10. "Group_name" al tener una etiqueta diferente en la web, no la reconoce y salta a la siguiente <br>
* Solución: analizamos solo los 9 próximos eventos en Madrid sobre tecnología. Incluímos un Limit = 9 en nuestra petición a la web. <br>

### 3. Merge 
Unimos los dos Dataframe para conocer la relación entre los miembros del grupo y los asistentes a los eventos. <br>
* Con la función Merge y la columna "Group_Name" unimos ambos dataset para que nos devuelva un dataset con: de los 9 próximos eventos en Madrid, los que el grupo aparezcan entre los primeros 100 en tecnología. <br>
* Tenemos las columnas de "Numbers_of_members" del grupo y "Audience" del evento concreto. 
* Para poder dividirlas tenemos que mdoificar los tipos de datos de ambas columnas y pasarlos a numérico. <br>
* No nos permite el cambio a tipo int de la columna "Numbers_of_members" solo de tipo float, por lo que no podemos hacer la división. <br>
* Resultado, conocemos el grupo, el evento, el número de miembros del grupo y el número de participantes al evento de los 7 próximos eventos en Madrid sobre tecnología. <br>




