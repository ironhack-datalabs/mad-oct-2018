# Web Project

## Obtener datos de una API usando Python
### 1. Elegir base de datos. 
Después de investigar varias API procedentes de los dos enlaces proporcionados en la práctica. Me he decicio por "Makeup API" (http://makeup-api.herokuapp.com/). Una API que no requiere autentificación y tiene diferentes datos de 930 productos de belleza de una web. <br>

### 2. Hipótesis (finalidad)
Supongamos que trabajamos para una marca de cosméticos y quiere lanzar al mercado un nuevo producto cosmético: Eyeshadow. <br>

El perfil de consumidor de la web es nuestro principal target: Mujer, entre 30-40 años, urbanita, poder adquisitivo medio, interés por las últimas tendencias en moda, preocupada por el aspecto físico y asidua a compras por internet. <br>

Queremos analizar los productos Eyeshadow en esta web. <br>


### 3. Exportar datos. 
Exportamos los datos a través del comando request, al ser un archivo JSON, nos podemos permitir normalizarlo a través de "json_normalize". Nos devuelve una tabla que aún no sabemos que tipo de datos. <br>
Para ello aplicamos .info y vemos que nuestro dataset es de clase Dataframe, con 931 entradas (filas) una por cada producto, y 19 columnas con información sobre: <br> 

### 4. Data Cleaning 

Eliminamos columnas con información que no es necesaria: api_featured_image, image_link, product_api_url. <br>

He intentado normalizar la columna de "product_colors"  de varias maneras a través de json.normalize. Es el punto donde me he atascado. <br>
ejemplo1: json_normalize(df['product_colors'])['colour_name', 'hex_value'] <br>
ejemplo2: works_data = json_normalize(data=df['id'], record_path='product_colors', meta=['brand', 'description', 'name', 'rating'])<br>

