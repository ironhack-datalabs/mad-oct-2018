# Lab | API Scavenger Game


### Off topic
Un problema que he tenido en el previo del ejercicio fue al intentar ejecutar este comando: 
```
$ curl -u albertogcmr: TOKENasdfgsdgd https://api.github.com/ironhack-datalabs > outpout.json
```
Detecto que hay 2 errores: 
1. el espacio entre ```albertogcmr: TOKENasdfgsdgd``` resultante de copiar-pegar el TOKEN desde el navegador
2. **ironhack-datalabs** debe ser **user**  
Quedando como resultado: 
```
$ curl -u albertogcmr:TOKENasdfgsdgd https://api.github.com/user > output.json
```

### Generamos archivos
Para crear un entorno de desarrollo correcto en el que haya TOKEN pero no se suban al repositorio hay que hacer algunas modificaciones respecto a los ejercicios anteriores
1. Crear un archivo **.env** cuyo contenido sea: 
```GITHUB_TOKEN = "TOKENasdfgsdgd"```
2. Crear un archivo **.gitignore** cuyo contenido sea:
```
ipynb_checkpoints
.env
__pycache__
.DS_Store
```
3. Crear un archivo **loadCredentials.py** cuya función es leer desde el archivo **.env** los TOKEN que correspondan y su contenido sea:
```
#https://github.com/theskumar/python-dotenv

import os
from dotenv import load_dotenv

def loadCredentials(loadVars):
    load_dotenv()
    obj = dict()
    for v in loadVars:
        obj[v] = os.getenv(v)
        if not obj[v]:
            raise ValueError("env var '%s' does not exist. Please create a .env file containing it" % (v))
    return obj

if __name__ == "__main__":
    requestKeys = ["GITHUB_TOKEN"]
    d = loadCredentials(requestKeys)
    print(d)
```
## Challenge 1: Fork Languages
Para obtener los lenguajes accedemos al recurso repositorios y observamos el dataframe que nos crea pandas: 
```
api_url_base = 'https://api.github.com'
repos = '/repos/ironhack-datalabs/madrid-oct-2018/forks'

req = requests.get(api_url_base + repos).json()
```
Para no saturar las peticiones al servidor y nos vete el acceso, cosa que ocurre con la IP de Ironhack, sólo lanzamos la petición una vez y almacenamos el resultado en req, para luego en otra celda poder crear el Dataframe todas las veces que queramos. 
```
forks = req
df_forks = pd.DataFrame(forks)
df_forks.head()
```
Con el siguiente comando vemos las columnas de nuestro DataFrame. 
```
df_forks.columns
```
Observamos que hay una columna **language** por lo que contamos los lenguajes unicos con la siguiente sentencia: 
```list(df_forks.language.unique())```
Y como resultado los lenguajes diferentes son: ```['HTML', 'Jupyter Notebook', 'Python']```


## Challenge 2: Count Commits
Tras varios intentos fallidos debidos a errores sintácticos cometidos en el filtrado, descubrimos leyendo la API dos cosas: 
1. El tamaño máximo de página por petición es 30 items. Lo cambiamos con **num_pages = '100'**
2. La sintaxis para varios criterios de filtrado es: 
```
url/recurso/?param1=123&param2=456&param3=789
```
Por lo que con el siguiente código filtramos por fecha inicial y final así como cambiamos el tamaño máximo de página a 100. 
```
# Datos del filtrado
init_date = '2018-10-20T00:00:00Z'
end_date = '2018-10-25T23:59:59Z'
num_pages = '100'
api_url_base = 'https://api.github.com'
recurso = '/repos/ironhack-datalabs/madrid-oct-2018/commits'

# Preparado de los parámetros
init_date_url = 'since='+init_date
end_date_url = 'until='+end_date
pages = 'per_page='+num_pages
filtros = '&'.join([init_date_url, end_date_url, pages])

# url final del recurso a consumir con sus parámetros según la API indica
url = api_url_base + recurso + '?' + filtros

req = requests.get(url).json()
```
Ya solo nos queda crear el DataFrame: 
```
df_comm = pd.DataFrame(req)
df_norm = json_normalize(df_comm['commit'])
print(len(df_norm))
```
Y como resultado obtenemos **21**


## Challenge 3: Hidden Cold Joke

Automatizamos las urls de las request que serán una lista de 24 elementos. 
1. Generamos 24 nombres \[.0001.scavengerhunt - .0001.scavengerhunt\]
```
def get_lista_names(name='scavengerhunt', mini=1, maxi=24): 
    res = []
    for x in range(mini, maxi+1): 
        numero_4_digitos = '{:04}'.format(x)
        res.append('.' + numero_4_digitos + '.' + name)
    return res
```
2. Generamos 24 urls completas para pasar a nuestro requests.get con el formato 'https://api.github.com/search/code?q=filename:.00XX.scavengerhunt+repo:ironhack-datalabs/madrid-oct-2018'
```
def get_lista_recursos(lista_names, url='https://api.github.com'): 
    res = []
    for x in lista_names: 
        res.append(url+'/search/code?q=filename:{}+repo:ironhack-datalabs/madrid-oct-2018'.format(x))
    return res
```
3. Realizamos las 24 peticiones parando cada 9 elementos porque está limitado en tiempo y cantidad. 
```
def get_recursos(lista_recursos): 
    res = []
    for i, peticion in enumerate(lista_recursos): 
        # res.append(requests.get(peticion).json()['items'][0]['html_url'])
        res.append(requests.get(peticion))
        if i in [9, 18, 26]: 
            time.sleep(60)
    return res
```
4. Asimismo nuestro resultado es parseado a json() elemento a elemento y luego (previa observación manual) llegamos al elemento que nos interesa mediante \['items']\[0]\['html_url'] que es lo que se devuelve en esta función: 
```
def get_urls(recursos): 
    res = []
    for x in recursos: 
        res.append(x.json()['items'][0]['html_url'])
    return res
```

5. Recorremos la lista de URLs donde se encuentran nuestros archivos a abrir y capturamos el contenido. 
```
res = []
for x in urls_recursos: 
    content = requests.get(x.json()['items'][0]['url']).json()['content']
    res.append(decode(content))
res
```
Cuya solución: 
```
[b'In\n',
 b'data\n',
 b'science,\n',
 b'80\n',
 b'percent\n',
 b'of\n',
 b'time\n',
 b'spent\n',
 b'is\n',
 b'preparing\n',
 b'data,\n',
 b'20\n',
 b'percent\n',
 b'of\n',
 b'time\n',
 b'is\n',
 b'spent\n',
 b'complaining\n',
 b'about\n',
 b'the\n',
 b'need\n',
 b'to\n',
 b'prepare\n',
 b'data.\n']
```
Que habrá que limpiar y pasar a utf-8

