# Importo todos los modulos a utilizar 
import requests
import pandas as pd
from pandas.io.json import json_normalize

# Request de la busqueda hecha para obtener el path de scavenger hunt
response = requests.get("https://api.github.com/search/code?q=filename:.scavengerhunt+repo:ironhack-datalabs/madrid-oct-2018").json()
df = pd.DataFrame(response)
a = json_normalize(df["items"])


# Loop para obtener todo el contenido de los ficheros con nombre scavenger, para el loop se utiliza el path
url_inic = "https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/"
content = "contents/"
list_names = []
list_codes = []
for i in a.path:
    req = requests.get(url_inic+content+i).json()
    list_names.append(req["name"])
    list_codes.append(req["content"])


# importamos modulo base64 para poder decodificar el contenido obtenido. 
import base64
dictio = {"names":list_names,"codes":list_codes}
df = pd.DataFrame(dictio)
df = df.sort_values(by =["names"])
list_cont = []
for i in df["codes"]: 
    list_cont.append(base64.b64decode(i).decode("utf-8").replace("\n",""))

mensaje = " ".join(list_cont)
print (mensaje)