## PIPELINE PROJECT

#Paso 1 
Importo las librerias necesarias para la ejecucion:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Eligo las bases de datos utilizados en mi pandas_project las cuales limpie previamente, como base ara mi pipeline.

#Paso 2
Defino un acquire el cual me va proporcionar los datos y tendra como salida todos los datos los cuales se utilizaran como entrada en mi proxima funcion.
En este paso creo un input donde establezco el año del que quiero definir los datos.

#Paso 3
con la entrada de datos ya establecida, defino un wrangle el cual filtrara a traves del año.

#Paso 4

Defino un nuevo filtro el cual establecera la media del Happiness Score segun el BIN en el que se encuentre (High, Medium, Low)

##Paso 5
Una vez obtenidos los datos ya filtrados de Happines Score Media segun su Bin creo un chart el cual se guardara automaticamente en mi ordenador a traves de la funcion save_viz la cual sigue una estructura parecida a visualize. Para crear este chart necesito definir x e y 

        ##Problemas : En este paso me he encontrado con varios problemas a la hora de definir los titulos 

##Paso 6
En este ultimo paso establezco las relaciones para crear mi pipeline y cuales son los elementos de entrada y salida de cada uno para que se pueda ejecutar 
