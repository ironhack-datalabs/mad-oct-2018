import requests
import pandas as pd
from pandas.io.json import json_normalize

# Hago la solicitud para obtener los forks para el repo en cuestion
response = requests.get("https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/forks")
result = response.json()

#  transformo el .json en un Dataframe y  filtro por language utilizando la funcion set para conseguir 
# los valores unicos. 

flattened_data = json_normalize(result)
data = pd.DataFrame(flattened_data)
languages = set(data["language"])
languages