###WEB PROJECT 

#API

##Paso 1
He importado las diferentes librerias necesarias. 
import json
import requests
import pandas as pd

##Paso 2
Una vez seleccionada la API (con la cual he tenido varios problemas al seleccionarla, principalmente por la falta de datoss en la mayoria de las que me importaba) 

En este caso el url que me importaba los datos era un json.


##Paso 3
He tratado de normalizar los datos aun que me han surgido problemas por la cantifdad de datos. luego he analizado los distintos tipos de df y he adecuado cada uno al tipo de categoria . 

##Paso 4 
He hecho a traves de un group by una agrupacion de las categorias y el tipo de currency y sacar el precio medio de cada uno.


##Paso 5 
En el paso 5 decido sacar los posibles elementos del tag list que tiene cada uno de los productos, es decir, dentro de cada producto podemos clasificarlos por su composicion o elementos. Y concluyo con un total de 7 tags en todo el dataframe en total de todos los productos. 

'''
df_tag= pd.DataFrame(df.tag_list.values.tolist(), df.index).add_prefix('tag_')
'''

Por lo que creo una columna para cada uno de los diferentes tags y lo concateno con el df total. Es decir me creo una tabla donde para cada elementp de la lista del tag list haya una coumna. 

''' 
df = pd.concat([df,df_tag],axis=1)
'''

##Paso 6 
Cuando saco la info del data total, con los diferentes tags ya incorporados, concluyo el nuero de tags por elementos ya que no todos los productos tienen las mismas caracteristicas. 

#Paso 7
Por otro lado he tenido que cambiar el tipo de cada uno de los tags a categries 

'''
df['tag_1'] = df['tag_1'].astype('category')
'''

Una vez hecho el cambio de tipo saco cada uno de los elementos de cada tag list 

Finaalmente determino que despues de haber separado las diferentes columnas de tags veo que de los 931 registros totales solo 199 tienen el primer elemneto del tag list y que no me va a ser util 

##Paso 8
Por otro lado he decidido hacer un group by donde he clasificado segun la categoria y el rating de cada uno a pesar de que muchos de ellos son nulos.

##WEB SCRAPING 

