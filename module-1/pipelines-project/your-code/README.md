# Pipeline - project

##  -- Procesos seguido --

## Input

Genero un loop de whiles para que te obligue a colocar el año y el mes correcto. 

IMPORTANTE: Solamente estan los archivos del 2016 y 2017 por lo que solo se puede probar con ellos. Si deseas ver los partidos ganados en todo el año y no separar por mes, en mes hay que colocar 0.

## Adquisicion de datos: 

Utilizo la funcion de pandas para poder importar los archivos, para que el archivo abra debe estar guardado bajo el formato ¨tenis_año.csv¨. 

IMPORTANTE: Solamente estan los archivos del 2016 y 2017 por lo que solo se puede probar con ellos. 

## Wranging: 
1) Eliminamos los valores que aparezcan como NAN en mas de 10 columnas para la misma fila
2) le damos formato datetime a la columna de "tourney_date" y creamos una nueva columna con el mes. 
3) Filtramos el DF por el mes que el usuario selecciono, en caso que haya seleccionado 0 obviamos ese paso. 

## Analyzing
1) Calculamos los 5 jugadores que mas partidos ganaron para el mes en cuestion con la respectiva cantidad
2) Calculamos el promedio de partidos ganados por mes de los mismos 5 jugadores, para ello hacemos un merge.

## Reporting
1) Lei un poco la documentacion de matplotlib y cree los graficos, son 2 graficos solapados entre si, donde se puede ver de forma clara la cantidad de partidos ganados en el mes por cada jugador asi como la cantidad de partidos promedio ganado si tomamos en cuenta todo el año.
